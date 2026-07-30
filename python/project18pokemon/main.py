'''
import random
from model.pokemon import Bulbasaur,Charmander,Squirtle

p1 = Bulbasaur()
p2 = Squirtle()
p3 = Charmander()
pokemon_list = [p1, p2, p3]
print("======= POKEMON GAME =======")
print("1번: 이상해씨, 2번: 꼬부기, 3번: 파이리")

user= pokemon_list[int(input("스타팅 포켓몬을 골라주세요! (1~3): ")) - 1]
com = random.choice(pokemon_list)

print(f"\n[배틀 시작!] 내 포켓몬: {user.name} VS 상대 포켓몬: {com.name}\n")
# 3. 배틀 루프
while user.hp > 0 and com.hp > 0:
  # 유저 공격
  user.attack(com)
  if com.hp <= 0:
    print(f"{com.name}이(가) 쓰러졌습니다! 유저 승리!")
    break

  # 컴퓨터 공격
  com.attack(user)
  if user.hp <= 0:
    print(f"{user.name}이(가) 쓰러졌습니다! 컴퓨터 승리!")
    break
'''
from manager import play_game, print_pokemon_list, select_user_pokemon, select_com_pokemon, attack, battle_start

play_game()
print_pokemon_list()
select_user_pokemon()
select_com_pokemon()
battle_start()
