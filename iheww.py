infliename = input("입력파일이름 : ")
outfilename = input("출력파일이름 : ")

infile = open(infliename+".txt","r")
outfile = open(outfilename+".txt","w")

sum = 0
count = 0

for line in infile :
    dailySale = int(line)
    sum += dailySale
    count += 1

outfile.write(f"총매출 = {sum} \n")
outfile.write(f"평균 일매출 = {sum/count}")

infile.close()
outfile.close()
#################################3

try :
    bar = int(input("나눠지는 수를 입력하세요 : "))
    foo = int(input("나누는 수를 입력하세요 : "))
    result = bar/foo
    print(f"{bar}를 {foo}로 나눈 결과는 {result}입니다.")
except ValueError :
    print("정수를 입력해야 합니다.")
except ZeroDivisionError :
    print("0으로 나눌 수 없습니다.")
except Exception as e:
    print(f"오류가 발생했습니다. {e}")
else :
    print("나누기 연산 성공!")
finally :
    print("프로그램을 종료합니다")
