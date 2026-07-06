from turtle import * #タートルグラフィックスを使う準備
shape("turtle") #亀の登場
col = ["orange","limegreen","gold","plum","tomato"] #色の名前を５つ用意
for i in range(5): #以下の３行を５回繰り返すこと
    color(col[i]) 
    circle(30) 
    left(190) #
done() 
