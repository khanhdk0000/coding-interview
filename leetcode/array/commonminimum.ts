function getCommon(nums1: number[], nums2: number[]): number {
    while (nums1.length && nums2.length) {
        if (nums1[0] === nums2[0]) {
            return nums1[0];
        }
        if (nums1[0] < nums2[0]) {
            nums1.shift();
        } else if (nums1[0] > nums2[0]) {
            nums2.shift();
        }
    }
    return -1;
};