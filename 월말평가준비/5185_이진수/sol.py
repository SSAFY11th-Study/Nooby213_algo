import sys
sys.stdin = open('input.txt')
arr = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101',
       '1110', '1111']
T = int(input())
for t in range(1, T + 1):
       N, hex_num = input().split()
       bin_num = ''
       for i in hex_num:
              if i.isdecimal():
                     bin_num += arr[int(i)]
              else:
                     bin_num += arr[ord(i) - 55]
       print(f'#{t} {bin_num}')
