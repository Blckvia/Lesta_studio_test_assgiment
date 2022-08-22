# 1. 
# def isEven(value): return value%2==0

def isEven(value):
    if value % 2 == 0:
        return 'even'
    return 'odd'
    
def isEven(value):
    return "odd" if value&1 else "even"

def isEven(value): return value&1==0

print(isEven(9))

# Три реализации предлагаю. В двух из примеров я использую побитовый оператор &. 
# Плюсы: легко читать и понимать код.
# Минусы: более медленная работа нежели у низкоуровневых операций.


# 2.

class Fifo:
    def __init__(self):
        self.mas = []

    def append_element(self, element):
        self.mas.append(element)

    def get_element(self):
        out = self.mas.pop(0) if self.mas else None

    def __str__(self):
        return '"%s"' % (self.mas)
        
        
        
class CircularBuffer(object):
    def __init__(self, size):
        self.index= 0
        self.size = size
        self._data = []

    def record(self, value):
        if len(self._data) == self.size:
            self._data[self.index]= value
        else:
            self._data.append(value)
        self.index= (self.index + 1) % self.size

    def __getitem__(self, key):
        return(self._data[key])

    def __repr__(self):
        return self._data.__repr__() + ' (' + str(len(self._data))+' items)'

    def get_all(self):
        return(self._data)
    
# 3. Я предпочел сортировку слиянием, быстрой сортировке так как в данном таске есть возможность, 
# что опорный элемент будет наименьшим или наибольшим элементом списка. Быстрая сортировка работаеет быстрее с более
# сбалансированными значениями. В отличии от сортировки кучи и сортировки слиянием, обе из которых имеют худшие времена
# O(nlog(n)), быстрая сортировка имеет худшее время O(n**2).

def mergeSort(nums):
    if len(nums)==1:
        return nums
    mid = (len(nums)-1) // 2
    lst1 = mergeSort(nums[:mid+1])
    lst2 = mergeSort(nums[mid+1:])
    result = merge(lst1, lst2)
    return result

def merge(lst1, lst2):
    lst = []
    i = 0
    j = 0
    while(i<=len(lst1)-1 and j<=len(lst2)-1):
        if lst1[i]<lst2[j]:
            lst.append(lst1[i])
            i+=1
        else:
            lst.append(lst2[j])
            j+=1
    if i>len(lst1)-1:
        while(j<=len(lst2)-1):
            lst.append(lst2[j])
            j+=1
    else:
        while(i<=len(lst1)-1):
            lst.append(lst1[i])
            i+=1
    return lst

        

        
        
