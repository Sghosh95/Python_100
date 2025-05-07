def calculate_love_score(name1,name2):
  word=name1+name2
  word=word.lower()
  t_count=word.count("t")
  r_count=word.count("r")
  u_count=word.count("u")
  e_count=word.count("e")
  first_digit=t_count+r_count+u_count+e_count

  l_count=word.count("l")
  o_count=word.count("o")
  v_count=word.count("v")
  e_count=word.count("e")
  second_digit=l_count+o_count+v_count+e_count

  love_score=int(str(first_digit)+str(second_digit))
  print(love_score)
  

calculate_love_score("Kanye West", "Kim Kardashian")