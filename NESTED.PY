#1. Nested - Ang "nested" kay nagpasabot nga nasa sulod sa usa ka structure. Mura siya ug box nga naay sulod nga box. 
# So, sa programming, kung naay usa ka loop, function, or condition nga nasa sulod sa lain, tawagon nato na siya nga nested
#Example: Mura siya ug nested na box, like big box and then naay gamay nga box sa sulod.

# Loop - Ang "loop" kay usa ka construct sa programming nga nagpasabot nga magbalik-balik ka sa usa ka block sa code. Useful ni siya para mag-automate sa mga repetitive tasks.
# Kung naa kay list of names, pwede ka mag-loop para i-print ang matag name without writing the print statement for each name.

#Nested Loop - Ang "nested loop" kay loop nga nasa sulod sa lain nga loop. Ang outer loop mo-run una, unya for each iteration sa outer loop, ang inner loop mag-run pud completely.

#Summary:
#Nested: Something na nasa sulod sa lain.
#Loop: Magsugod ug balik-balik sa code.
#Nested Loop: Loop nga nasa sulod sa lain nga loop, allowing you to work with combinations or multiple datasets.

#Output Structure
#Ang output nga imo gi-provide kay nag-represent sa combinations sa duha ka lists (or arrays). Let’s break it down.

#EXAMPLE
list1 = [1, 2, 3]
list2 = [4, 5, 6]

for i in list1:  # Outer loop para sa list1
    for j in list2:  # Inner loop para sa list2
        print(i, j)  # I-print ang current pair
    print()  # Newline after each outer loop iteration

#Breakdown sa Output
#Outer Loop:
#Ang outer loop (for i in list1) nag-iterate sa matag element sa list1.

#For example:
       #First iteration: i is 1
       #Second iteration: i is 2
       #Third iteration: i is 3

#Inner Loop:
    #Para sa matag value sa i (gikan sa list1), ang inner loop (for j in list2) nag-iterate sa tanan elements sa list2.
    #So, kung i is 1, ang inner loop mo-run ug j will take values 4, 5, 6, resulting in:
 
1 4
1 5
1 6

#Newline After Each Outer Loop:
        # Pagka-human sa inner loop, ang print() mag-insert ug newline para mas klaro ang output.
         # This way, each group of results sa i will be separated, producing:

2 4
2 5
2 6

3 4
3 5
3 6

#Final Output Structure
#So, ang complete output kay ingon ani:


1 4
1 5
1 6

2 4
2 5
2 6

3 4
3 5
3 6

#Summary
#Ang kada pair sa output kay nag-represent sa combination sa element gikan sa list1 ug list2.
#Ang una nga number (from list1) mag-change kada iteration sa outer loop.
#Ang ikaduhang number (from list2) mo-run sa tanan values for each corresponding value sa una nga number.
#Ang newline nag-separate sa mga groups para mas klaro.