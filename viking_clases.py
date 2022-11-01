
import random



# Soldier

class Soldier(object):
    
    def __init__(self, health, strength):        #Se puede inicializar en un dato que te dé el usuario
        self.health =  health;
        self.strength = strength;
        
        
    def attack(self):
        
        return self.strength;
        
        
        
    def receive_damage(self, damage):
        self.health -= damage;
        return
        


# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        self.name =  name;
        self.health =  health;
        self.strength = strength;
    
    
    def receive_damage(self, damage):
        self.health -= damage;
        if self.health <= 0:
            result = (f"{self.name} has died in act of combat");
            
        elif self.health>0:
            result = (f"{self.name} has received {damage} points of damage");
        
        return result;
    
    def battle_cry(self):
        return ('Odin Owns You All!');
        
    


# Saxon


class Saxon(Soldier):
    
    
    def __init__(self, health, strength):        
        self.health =  health;
        self.strength = strength;
    
    
    def receive_damage(self, damage):
        self.health -= damage;
        if self.health <= 0:
            result = ("A Saxon has died in combat");
            
        elif self.health>0:
            result = (f"A Saxon has received {damage} points of damage");
        
        return result;
    
    
    


# War


class War(object):
    
    def __init__(self):
        self.viking_army = [];
        self.saxon_army = [];
    
    def show_viking(self, numero):
        return (self.viking_army[numero].name,self.viking_army[numero].health, self.viking_army[numero].strength);
        
        
    def add_viking(self, Viking):
        self.viking_army.append(Viking);
        return;
    
    def add_saxon(self, Saxon):
        self.saxon_army.append(Saxon);
        return;
    
    def viking_attack(self):
        
        r1=random.randint(0,(len(self.saxon_army)-1));
        r2=random.randint(0,(len(self.viking_army)-1));
        
        r_b1 = self.saxon_army[r1].receive_damage(self.viking_army[r2].strength);
        
        if self.saxon_army[r1].health<=0:
            self.saxon_army.pop(r1)
        
        
        return r_b1;
    
    def saxon_attack(self):
        r1=random.randint(0,(len(self.viking_army)-1));
        r2=random.randint(0,(len(self.saxon_army)-1));
                
        r_b2 = self.viking_army[r1].receive_damage(self.saxon_army[r2].strength);
        
        if self.viking_army[r1].health<=0:
            self.viking_army.pop(r1)
        
        
        return r_b2;
    
    def show_status(self):
        if len(self.saxon_army)==0:
            r_w =('Vikings have won the war of the century!');
            
        elif len(self.viking_army)==0:
            r_w =('Saxons have fought for their lives and survive another day...');
            
        else:
            r_w =('Vikings and Saxons are still in the thick of battle.');
            
            
        return r_w;    
            


