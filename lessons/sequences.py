"""Notes and examples of tuple and range sequence types """


#Declaring a type alias that "invents" the Point2D type
Point2D = tuple[float, float]

start_position: Point2D = (5.0, 10,0)
start_position = (start_position[0] + 5.0, start_position[1] + 10.0)
end_position: Point2D = (99.0, 99.0)

#tupes bc they are a sequence are 0-indexed
print(start_position[0])

for item in end_position:
    print(item)

#Examples of ranges 
a_range: range = range(0, 10, 1)
#access its items: 
print(a_range[0])
print(a_range[1])
print(len(a_range))
for i in a_range:
    print(i)

#An examples of usin the defaule paramater step
#whre the default step is 1
another_range: range = range(0, 10)

#if you only pass one argument to a range, it specifices 
#the stop marker and start is 0 by default 
zero_start: range = range(10)
for x in zero_start:
    print(x)

names: list[str] = ["kriss","Alyssa", "Ben,", "Arnold"]

for name in names:
    print(name)

#Range is often used to write for loops where
#your iteration patter is not consecutive
print("Every other")
for i in range (0, len(names), 2):
    print(names[i])

