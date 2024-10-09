def my_sum(my_list):#python在进行函数传参的时候，不用写参数的类型
    if len(my_list) == 1:
        return my_list[0]#作用：如果list只有一个元素，就直接返回值；使函数达到“归”的条件
    else:
        return my_list[0] + my_sum(my_list[1:])#这里是让每次输入给函数的list返回 首个和剩余值的和，
    
if __name__ == "__main__":
    print(my_sum([1,2,3,4,5]))