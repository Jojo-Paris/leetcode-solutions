class�Solution:
����def�characterReplacement(self,�s:�str,�k:�int)�->�int:
��������count�=�{}
��������res,�l,�maxFreq�=�0,�0,�0

��������for�r�in�range(len(s)):
������������count[s[r]]�=�count.get(s[r],�0)�+�1
������������maxFreq�=�max(maxFreq,�count[s[r]])
������������while�(r�-�l�+�1)�-�maxFreq�>�k:
����������������count[s[l]]�-=�1
����������������l�+=�1

������������res�=�max(res,�r�-�l�+�1)
��������return�res
������������

������������

"ABAB"
