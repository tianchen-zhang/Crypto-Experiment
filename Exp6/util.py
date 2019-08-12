# 各种常用函数
S_BOX = [[99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118], 
[202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192], 
[183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21], 
[4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117], 
[9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132], 
[83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207], 
[208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168], 
[81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210], 
[205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115], 
[96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219], 
[224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121], 
[231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8], 
[186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138], 
[112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158], 
[225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223], 
[140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22]]

REV_S_BOX = [[82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 215, 251], 
[124, 227, 57, 130, 155, 47, 255, 135, 52, 142, 67, 68, 196, 222, 233, 203], 
[84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250, 195, 78], 
[8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37], 
[114, 248, 246, 100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146], 
[108, 112, 72, 80, 253, 237, 185, 218, 94, 21, 70, 87, 167, 141, 157, 132], 
[144, 216, 171, 0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6], 
[208, 44, 30, 143, 202, 63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107], 
[58, 145, 17, 65, 79, 103, 220, 234, 151, 242, 207, 206, 240, 180, 230, 115], 
[150, 172, 116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28, 117, 223, 110], 
[71, 241, 26, 113, 29, 41, 197, 137, 111, 183, 98, 14, 170, 24, 190, 27], 
[252, 86, 62, 75, 198, 210, 121, 32, 154, 219, 192, 254, 120, 205, 90, 244], 
[31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236, 95], 
[96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239], 
[160, 224, 59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131, 83, 153, 97], 
[23, 43, 4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33, 12, 125]]

mixColumnTable = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]
revMixColumnTable = [[14, 11, 13, 9], [9, 14, 11, 13], [13, 9, 14, 11], [11, 13, 9, 14]]

RC = [1, 2, 4, 8, 16, 32, 64, 128, 27, 54]
# 整数转换为固定长度十六进制字符串
def int_to_hex(integer, length):
    #return ('{:0' + str(length) + 'x}').format(integer)
    return ('%0' + str(length) + 'x')%(integer)

# 整数转换为8bit二进制字符串
def int_to_bin(integer):
    return '{:08b}'.format(integer)

def hex_to_bin(string):
    return int_to_bin(int(string, 16))

def str_to_8bitList(string):
    return [int(string[i:i+2], 16) for i in range(0, len(string), 2)]

# 加法就是异或
def add(elm1, elm2):
    num1 = int(elm1, 2)
    num2 = int(elm2, 2)
    return '{:08b}'.format(num1 ^ num2)
# 减法同加法
def sub(elm1, elm2):
    return add(elm1, elm2)

# 一种移位乘法
def multiply(elm1, elm2):
    elm2 = elm2[: : -1]
    result = 0
    temp = int(elm1, 2)
    for i in range(8):
        if elm2[i] == '1':
            result ^= temp
        str_temp = '{:08b}'.format(temp)
        # 取模
        if str_temp[0] == '1':
            temp = int(str_temp[1: ] + '0', 2) ^ int("0x1B", 16)
        else:
            temp = int(str_temp[1: ] + '0', 2)
    return '{:08b}'.format(result)


# 加法就是异或
def add(elm1, elm2):
    num1 = int(elm1, 2)
    num2 = int(elm2, 2)
    return '{:08b}'.format(num1 ^ num2)
# 减法同加法
def sub(elm1, elm2):
    return add(elm1, elm2)
'''
# 打表
multi = [0] * 256
multi[0] = 1
# 生成元表
for i in range(1, 255):
    multi[i] = (multi[i - 1] << 1) ^ multi[i - 1]
    if multi[i] & 0x100:
        multi[i] ^= 0x11B
# 生成元反表
arc_multi = [0] * 256
for i in range(255):
    arc_multi[multi[i]] = i
# 逆表
reverse = [0] * 256
for i in range(1, 256):
    reverse[i] = multi[(255 - arc_multi[i]) % 255]

# 打表求解乘除和逆
def multiply(elm1, elm2):
    return '{:08b}'.format(
        multi[(arc_multi[int(elm1, 2)] + arc_multi[int(elm2, 2)]) % 255])
def rev(elm):
    return '{:08b}'.format(reverse[int(elm, 2)])
def divide(elm1, elm2):
    return table_multiply(elm1, table_rev(elm2))
'''
if __name__ == '__main__':
    print(int_to_hex(1, 2))
    print(S_BOX[253//16][253%16])
    print(int(multiply(int_to_bin(253), "00001110"), 2))
    print(int(multiply(int_to_bin(13), "00001011"), 2))
    print(int(multiply(int_to_bin(66), "00001101"), 2))
    print(int(multiply(int_to_bin(203), "00001001"), 2))