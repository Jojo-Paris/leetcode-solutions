class�Solution:
����def�sumOddLengthSubarrays(self,�arr:�List[int])�->�int:
��������ans=0
��������n=�len(arr)
��������for�i�in�range�(n):
������������for�j�in��range�(i+1,n+1):
����������������if�(j-i)%2:
��������������������ans+=sum�(arr[i:j])

����������������
��������return�ans
[1,4,2,5,3]