# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import torch


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import sys, platform

    print(sys.platform)
    print(platform.system()=='Windows')
    # print_hi('PyCharm')
    # a = torch.randn(3, 5)
    # print(a)
    # b= a.view(3,1,5)
    # c= a.view(3,1,5).repeat(1,5,1)
    # print(b)
    # print(b.shape)
    # print(c)
    # print(c.shape)

    print((torch.rand([1,2])<0).int())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
