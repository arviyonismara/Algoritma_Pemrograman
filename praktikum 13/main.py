from kasus1 import*
def main():
    v1 = Vector2D(1,2)
    v2 = Vector2D(3,4)
    v3 = v1+v2
    v4 = v1-v2
    v5 = v1*v2
    v6 = abs(v4)
    print('v1 :',v1.x,v1.y)
    print('v2 :',v2.x,v2.y)
    print('v3 :',v3.x,v3.y)
    print('v4 :',v4.x,v4.y)
    print('v5 :',v5.x,v5.y)
    print('v6 :',v6)
    print(v1 == v4)
    print(Vector2D(1,0) == Vector2D(1,0))

if __name__ == "__main__":
    main()