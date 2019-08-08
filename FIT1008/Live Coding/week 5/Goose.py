class Goose:
    def __init__(self,health,damageBite,currentContents,colour):
        self.HP = health
        self.biteDamage = damageBite
        self.processedSubstrateVolumeInColon = currentContents
        self.featherColour = colour
        self.fainted = False
    
    def __str__(self):
        return str(self.HP)+" fainted? "+str(self.fainted)
    
    def attack(self,otherGoose):
        #self.hiss()
        if otherGoose.HP <= self.biteDamage:
            otherGoose.fainted = True
            otherGoose.HP = 1
        else:
            otherGoose.HP -= self.biteDamage
        
    def poop(self):
        print("has voided: "+str(self.processedSubstrateVolumeInColon))
        self.processedSubstrateVolumeInColon=0
        
LucyGoosey = Goose(10,3,20,"brown")
GoosemanEtGomez = Goose(10,5,20,"yellow")
#print(LucyGoosey)
#print(GoosemanEtGomez)

#test 1 attack with both positive HP and positive damage (< HP)
GoosemanEtGomez.attack(LucyGoosey)
print("Lucy",LucyGoosey)
print("GYG",GoosemanEtGomez)
#expect HP of lucy = 5

#test 2 attack where dmg = HP remaining
GoosemanEtGomez.attack(LucyGoosey)
print("Lucy",LucyGoosey)
print("GYG",GoosemanEtGomez)
#expect HP = 1, fainted is true

#test 3 attack where already fainted
GoosemanEtGomez.attack(LucyGoosey)
print("Lucy",LucyGoosey)
print("GYG",GoosemanEtGomez)
#expect no change made to either instance

