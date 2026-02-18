from matplotlib import pyplot as plt
country=['India','USA','Germany']
case=[100,200,300]
plt.bar(country,case,color=['red','blue','green'])
plt.show()

#Histrogram
population_age =[22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]

bins = [0,10,20,30,40,50,60,70,80,90,100.110,120]

plt.hist(population_age, bins, histtype='bar', rwidth=0.5)

plt.xlabel('age groups')

plt.ylabel('Number of people')

plt.title('Histogram')

plt.show()

#Scatter PLot

x = [1,1.5,2,2.5,3,3.5,3.6]

y = [7.5,8,8.5,9,9.5,10,10.5]

x1=[8,8.5,9,9.5,10,10.5,11]

y1=[3,3.5,3.7,4,4.5,5,5.2]

plt.scatter(x,y, label='high income low saving',color='g')

plt.scatter(x1,y1,label='low income high savings',color='y')

plt.xlabel('saving*100')

plt.ylabel('income*1000')

plt.title('Scatter Plot')

plt.legend()

plt.show()

