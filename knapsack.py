
import pprint
import numpy as np
items = {"stereo":{"price":3000,"mass":4},
            "laptop":{"price":2000,"mass":3},
            "guitar":{"price":1500,"mass":1}}
matrix = np.zeros((3,4))
matrix_items = np.empty([3,4],dtype="S30")
row_map ={0:"stereo",1:"laptop",2:"guitar"}
column_map ={0:1,1:2,2:3,3:4}
for row in row_map:
    print(f" Row = {row_map[row]}")
    print("-------------------------------")
    for column in column_map:
        print(f" Column = {column_map[column]}")
        if row >0:
            opt1=matrix[row-1][column]
            if items[row_map[row]]["mass"] <= column_map[column]:
                cur_price=items[row_map[row]]["price"]
                cur_mass=items[row_map[row]]["mass"]
                rem_mass = column_map[column]-cur_mass
                if rem_mass in column_map.values():
                    
                    opt2=cur_price+matrix[row-1][rem_mass-1]
                    #matrix_items[row][column] =matrix_items[row][column]+row_map[row]
                    

                else:
                    opt2=cur_price
                    #matrix_items[row][column] =matrix_items[row][column]+row_map[row]
            else:
                opt2=0
        else:
            cur_price=items[row_map[row]]["price"]
            cur_mass=items[row_map[row]]["mass"]
            if cur_mass <=column_map[column]:
                opt1,opt2=cur_price,cur_price
                matrix_items[row][column] =row_map[row]
            else:
                opt1,opt2=0,0

        print(opt1,opt2)

        matrix[row][column] =max(opt1,opt2 )

print(matrix)
print(matrix_items)
                

if __name__ == "__main__":
    items = {"stereo":{"price":3000,"mass":4},
            "laptop":{"price":2000,"mass":3},
            "guitar":{"price":1500,"mass":1}}
    limit = 4
    