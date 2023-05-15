import pygame
pygame.mixer.init()
import time
d={'1:The International Literacy Day is observed on': 'A.Sep 8  B.Nov 28  C.May 2  D.Sep 22', '2:The language of Lakshadweep, a Union Territory of India, is':'A.Tamil  B.Hindi  C.Malayalam  D.Telugu', '3:In which group of places the Kumbha Mela is held every twelve years?':'A.Ujjain, Purl, Prayag, Haridwar \nB.Prayag, Haridwar, Ujjain, Nasik\nC.Rameshwaram, Purl, Badrinath, Dwarika\nD.Chittakoot, Ujjain, Prayag,Haridwar','4:Bahubali festival is related to':'A.Islam  B.Hinduism  C.Buddhism  D.Jainism','5:Which day is observed as the World Standards Day?':'A.June 26  B.Oct 14  C.Nov 15  D.Dec 2','6:Which of the following was the theme of the World Red Cross and Red Crescent Day?':'A.Dignity for all - focus on women\nB.Dignity for all - focus on Children\nC.Focus on health for all \nD.Nourishment for all-focus on children', '7:September 27 is celebrated every year as':'A.Teachers Day  B.National Integration Day \nC.World Tourism Day  D.International Literacy Day', '8:Who is the author of Manas Ka-Hans?':'A.Khushwant Singh  B.Prem Chand \nC.Jayashankar Prasad  D.Amrit Lal Nagar', '9:The death anniversary of which of the following leaders is observed as Martyrs Day?':'A.Smt. Indira Gandhi  B.PI. Jawaharlal Nehru  \nC.Mahatma Gandhi  D.Lal Bahadur Shastri', '10: Who is the author of the epic Meghdoot?':'A.Vishakadatta  B.Valmiki  C.Banabhatta  D.Kalidas'}
print('Currently you have 0 Rupees. But you can win upto 1 Crore Rupees\nYou will get 10 lakh Rs for every question')
q=list(d.keys())
a=list(d.values())
ans=['a','c','b','d','b','b', 'c', 'd', 'c','d']
t_ans=['A.Sep 8', 'C.Malayalam', 'B.Prayag, Haridwar, Ujjain, Nasik', 'D.Jainism', 'B.Oct 14', 'B.Dignity for all - focus on Children', 'D.Amrit Lal Nagar', 'C.World Tourism Day', 'C. Mahatma Gaandhi', 'D.Kalidas']
marks=0
count=0

while(True):
  print('\n**********Welcome to Kaun Banegaa Crorepati\n')
  pygame.mixer.music.load('Kbc Theme-[AudioTrimmer.com].mp3')
  pygame.mixer.music.play()
  time.sleep(6)
  for i in ans:
    print(f'\nOur question {count+1} is\n\n{q[count]}\n{a[count]}\n')
    u=input('Your Answer?')
    if u in i:
      print('Your answer is right!')
      marks+=10
      print(f'You have {marks} Lakh Rupees now')
      pygame.mixer.music.load('Kbc Correct Answer - Sound ! Notification.mp3')
      pygame.mixer.music.play()
      time.sleep(1)
    else:
      print(f'Oops the correct answer is {t_ans[count]}')
      pygame.mixer.music.load('Kbc - Wrong Answer Sound.mp3')
      pygame.mixer.music.play()
      time.sleep(3)
      print(f'\nCongratulations u got {marks} Lakh Rupees. Well Played! Thanks for playing the Quiz:)')
      break
    count+=1
  if marks==100:
    print(f'\nCongratulations u got 1 Crore Rupees. You are the Best.Thanks for playing the Quiz:)')
    pygame.mixer.music.load('Kbc Theme-[AudioTrimmer.com].mp3')
    pygame.mixer.music.play()
    time.sleep(5)

  x=int(input('\nWant to play again?\nType 1 for yess and 2 for no\n'))
  if x==1:
    count=0
    marks=0
    continue
  else:
    print('Thanks for playing the KBC, The hub of ultimate knowledge\n')
    break
