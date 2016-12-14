# Nicolas Mauger, 11/12/16 release under WTFPL License
# On utilisera dans cet exemple la bibliotheque de programmation lineaire "pulp"
# Cela n'a donnc aucun interet algorithmique, il donne juste le bon exemple
# Toute la documentation disponible sur https://www.coin-or.org/PuLP/index.html

# On reprendra ici l'exemple du chapitre 1 : Z(x,y) = (3/2)x + y
# 3x + 2y <= 6
# x + y <= 8
# 0 <= y <= 4
# x <= 1

# la ligne suivante importe la bibliotheque pulp
import pulp

# on peut tester l'installation avec la commande pulp.pulpTestAll()

# Definition du probleme, on choisi ici si l'on minimise ou maximise la fonction
# On utilisera "LpMaximize" dans le cas d'une maximisation
exemple = pulp.LpProblem(u"exemple du chapitre 1", pulp.LpMinimize)

# variables (continues de valeur minimale 0)
x1 = pulp.LpVariable("x1",0)
x2 = pulp.LpVariable("x2",0)

# Voici la fonction a maximiser
exemple += 1.5*x1 + x2
exemple.objective.setName('z')

# et voila les contraintes
exemple += 3*x1 + 2*x2      <=  6 , u"contrainte a"
exemple += x1   + x2        <=  8 , u"contrainte b"
exemple += x2               >=  0 , u"contrainte c"
exemple += x2               <=  4 , u"contrainte d"
exemple += x1               <=  1 , u"contrainte e"

# Affichons pour verifier
print (exemple)

# La resolution
exemple.solve()
exemple.objective.setName("z")
# bug : sans cette commande exemple.objective.name vaut 'OBJ' et non 'z'...
print(pulp.LpStatus[exemple.status], " : " , pulp.LpSenses[exemple.sense])
print("%3s <- %s"%(exemple.objective.name, pulp.value(exemple.objective)))
for var in exemple.variables() :
    print("%3s <- %s"%(var,pulp.value(var)))

# Et ... c'est tout ! Bravo, vous savez maintenant utiliser la librairie Pulp !
