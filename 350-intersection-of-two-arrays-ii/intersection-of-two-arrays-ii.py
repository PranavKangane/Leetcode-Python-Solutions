class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final =  list(set(nums1) & set(nums2))
        print(final)
        f1 = []
        for x in range(len(final)):
            n1 = nums1.count(final[x])
            n2 = nums2.count(final[x])
            a = min(n1,n2)
            print(a)
            for i in range(a):
                f1.append(final[x])
                print(f1)
        
        return f1