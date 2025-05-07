scores=[5,1,3,45,5,6,7,78,90]
sum=0
for score in scores:
    sum+=score
print(sum)

# total_score=sum(scores)
# print(total_score)


max=0
for elements in scores:
    if elements>max:
        max=elements
print(max)
