# --------------------------------------------
# Time      : Fri Sep 24 14:45:54 2021
# Note      : Ciaahh ! Mau ngapain ? Kentot
# --------------------------------------------
import codecs,base64

htr = [73, 121, 65, 116, 75, 105, 48, 103, 89, 50, 57, 107, 97, 87, 53, 110, 79, 105, 66, 49, 100, 71, 89, 116, 79, 67, 65, 116, 75, 105, 48, 75, 73, 121, 66, 66, 100, 88, 82, 111, 98, 51, 73, 103, 79, 105, 66, 76, 97, 87, 53, 110, 100, 71, 86, 105, 90, 81, 111, 106, 73, 69, 78, 112, 90, 87, 85, 103, 89, 87, 82, 104, 73, 72, 108, 104, 98, 109, 99, 103, 90, 71, 86, 106, 98, 50, 82, 108, 73, 71, 53, 112, 97, 67, 65, 104, 73, 71, 70, 111, 89, 87, 104, 104, 97, 65, 112, 112, 98, 88, 66, 118, 99, 110, 81, 103, 98, 51, 77, 115, 99, 51, 108, 122, 76, 72, 74, 108, 76, 71, 108, 117, 97, 83, 120, 122, 101, 88, 77, 115, 100, 71, 108, 116, 90, 83, 120, 113, 99, 50, 57, 117, 76, 72, 74, 108, 99, 88, 86, 108, 99, 51, 82, 122, 67, 110, 82, 121, 101, 84, 111, 75, 67, 87, 108, 116, 99, 71, 57, 121, 100, 67, 66, 119, 101, 88, 82, 108, 99, 51, 78, 108, 99, 109, 70, 106, 100, 65, 111, 74, 90, 110, 74, 118, 98, 83, 66, 112, 98, 121, 66, 112, 98, 88, 66, 118, 99, 110, 81, 103, 81, 110, 108, 48, 90, 88, 78, 74, 84, 119, 111, 74, 90, 110, 74, 118, 98, 83, 66, 107, 89, 88, 82, 108, 100, 71, 108, 116, 90, 83, 66, 112, 98, 88, 66, 118, 99, 110, 81, 103, 90, 71, 70, 48, 90, 88, 82, 112, 98, 87, 85, 75, 67, 87, 90, 121, 98, 50, 48, 103, 89, 110, 77, 48, 73, 71, 108, 116, 99, 71, 57, 121, 100, 67, 66, 67, 90, 87, 70, 49, 100, 71, 108, 109, 100, 87, 120, 84, 98, 51, 86, 119, 67, 103, 108, 109, 99, 109, 57, 116, 73, 70, 66, 74, 84, 67, 66, 112, 98, 88, 66, 118, 99, 110, 81, 103, 83, 87, 49, 104, 90, 50, 85, 115, 86, 87, 53, 112, 90, 71, 86, 117, 100, 71, 108, 109, 97, 87, 86, 107, 83, 87, 49, 104, 90, 50, 86, 70, 99, 110, 74, 118, 99, 103, 112, 108, 101, 71, 78, 108, 99, 72, 81, 54, 67, 103, 108, 74, 98, 88, 66, 118, 99, 110, 82, 70, 99, 110, 74, 118, 99, 106, 112, 108, 101, 71, 108, 48, 75, 67, 74, 99, 98, 107, 49, 118, 90, 72, 86, 115, 90, 83, 66, 79, 98, 51, 81, 103, 83, 87, 53, 122, 100, 71, 70, 115, 98, 71, 86, 107, 73, 67, 70, 99, 98, 105, 73, 112, 67, 103, 112, 104, 73, 68, 48, 103, 74, 49, 119, 119, 77, 122, 78, 98, 77, 84, 115, 122, 77, 71, 48, 110, 67, 109, 48, 103, 80, 83, 65, 110, 88, 68, 65, 122, 77, 49, 115, 120, 79, 122, 77, 120, 98, 83, 99, 75, 99, 67, 65, 57, 73, 67, 100, 99, 77, 68, 77, 122, 87, 122, 69, 55, 77, 122, 100, 116, 74, 119, 112, 111, 73, 68, 48, 103, 74, 49, 119, 119, 77, 122, 78, 98, 77, 84, 115, 122, 77, 109, 48, 110, 67, 109, 115, 103, 80, 83, 65, 110, 88, 68, 65, 122, 77, 49, 115, 120, 79, 122, 77, 122, 98, 83, 99, 75, 89, 121, 65, 57, 73, 67, 100, 99, 77, 68, 77, 122, 87, 122, 69, 55, 77, 122, 90, 116, 74, 119, 112, 54, 73, 68, 48, 103, 74, 49, 119, 119, 77, 122, 78, 98, 77, 84, 115, 122, 77, 50, 49, 99, 77, 68, 77, 122, 87, 122, 69, 119, 77, 87, 48, 110, 67, 110, 107, 103, 80, 83, 65, 110, 88, 68, 65, 122, 77, 49, 115, 119, 98, 83, 99, 75, 67, 109, 78, 115, 89, 88, 78, 122, 73, 70, 70, 104, 99, 50, 104, 105, 97, 88, 82, 122, 79, 103, 111, 75, 67, 87, 82, 108, 90, 105, 66, 51, 89, 87, 116, 48, 100, 83, 104, 122, 90, 87, 120, 109, 76, 72, 78, 108, 89, 50, 57, 117, 90, 67, 107, 54, 67, 103, 107, 74, 100, 50, 104, 112, 98, 71, 85, 103, 99, 50, 86, 106, 98, 50, 53, 107, 79, 103, 111, 74, 67, 81, 108, 116, 97, 87, 53, 122, 76, 72, 78, 108, 89, 51, 77, 103, 80, 83, 66, 107, 97, 88, 90, 116, 98, 50, 81, 111, 99, 50, 86, 106, 98, 50, 53, 107, 76, 68, 89, 119, 75, 81, 111, 74, 67, 81, 108, 48, 97, 87, 49, 108, 99, 105, 65, 57, 73, 67, 73, 103, 73, 70, 119, 119, 77, 122, 78, 98, 77, 84, 115, 122, 77, 50, 51, 105, 108, 114, 89, 103, 88, 68, 65, 122, 77, 49, 115, 120, 79, 122, 77, 51, 98, 86, 100, 104, 97, 88, 82, 112, 98, 109, 99, 103, 88, 68, 65, 122, 77, 49, 115, 120, 79, 122, 77, 51, 98, 101, 75, 102, 113, 70, 119, 119, 77, 122, 78, 98, 77, 84, 115, 122, 77, 109, 49, 55, 79, 106, 65, 121, 90, 72, 48, 54, 101, 122, 111, 119, 77, 109, 82, 57, 88, 68, 65, 122, 77, 49, 115, 120, 79, 122, 77, 51, 98, 101, 75, 102, 113, 83, 65, 105, 76, 109, 90, 118, 99, 109, 49, 104, 100, 67, 104, 116, 97, 87, 53, 122, 76, 72, 78, 108, 89, 51, 77, 112, 67, 103, 107, 74, 67, 88, 66, 121, 97, 87, 53, 48, 75, 72, 82, 112, 98, 87, 86, 121, 76, 71, 86, 117, 90, 68, 48, 105, 88, 72, 73, 105, 75, 81, 111, 74, 67, 81, 108, 48, 97, 87, 49, 108, 76, 110, 78, 115, 90, 87, 86, 119, 75, 68, 69, 112, 67, 103, 107, 74, 67, 88, 78, 108, 89, 50, 57, 117, 90, 67, 65, 116, 80, 83, 65, 120, 67, 103, 111, 74, 90, 71, 86, 109, 73, 69, 70, 49, 100, 71, 57, 102, 81, 50, 70, 119, 100, 71, 78, 111, 89, 83, 104, 122, 90, 87, 120, 109, 76, 72, 78, 108, 99, 122, 49, 121, 90, 88, 70, 49, 90, 88, 78, 48, 99, 121, 53, 84, 90, 88, 78, 122, 97, 87, 57, 117, 75, 67, 107, 112, 79, 103, 111, 74, 67, 87, 78, 118, 98, 109, 90, 112, 90, 121, 65, 57, 73, 71, 108, 117, 97, 83, 53, 119, 89, 88, 74, 122, 90, 83, 104, 118, 99, 71, 86, 117, 75, 67, 74, 106, 90, 109, 99, 117, 97, 87, 53, 112, 73, 105, 107, 117, 99, 109, 86, 104, 90, 67, 103, 112, 75, 81, 111, 74, 67, 87, 104, 108, 90, 71, 86, 121, 73, 68, 48, 103, 101, 119, 111, 74, 67, 81, 107, 105, 100, 88, 78, 108, 99, 105, 49, 104, 90, 50, 86, 117, 100, 67, 73, 54, 89, 50, 57, 117, 90, 109, 108, 110, 87, 121, 74, 107, 89, 88, 82, 104, 73, 108, 49, 98, 73, 110, 86, 122, 90, 88, 73, 116, 89, 87, 100, 108, 98, 110, 81, 105, 88, 83, 119, 75, 67, 81, 107, 74, 73, 109, 78, 118, 98, 50, 116, 112, 90, 83, 73, 54, 89, 50, 57, 117, 90, 109, 108, 110, 87, 121, 74, 107, 89, 88, 82, 104, 73, 108, 49, 98, 73, 109, 78, 118, 98, 50, 116, 112, 90, 83, 74, 100, 76, 65, 111, 74, 67, 81, 108, 57, 67, 103, 107, 74, 100, 50, 104, 112, 98, 71, 85, 103, 86, 72, 74, 49, 90, 84, 111, 75, 67, 81, 107, 74, 99, 71, 70, 110, 90, 83, 65, 57, 73, 72, 78, 108, 99, 121, 53, 110, 90, 88, 81, 111, 73, 109, 104, 48, 100, 72, 66, 122, 79, 105, 56, 118, 99, 87, 70, 122, 97, 71, 74, 112, 100, 72, 77, 117, 89, 50, 57, 116, 76, 121, 73, 115, 97, 71, 86, 104, 90, 71, 86, 121, 99, 122, 49, 111, 90, 87, 82, 108, 99, 105, 107, 75, 67, 81, 107, 74, 99, 50, 57, 49, 99, 67, 65, 57, 73, 69, 74, 108, 89, 88, 86, 48, 97, 87, 90, 49, 98, 70, 78, 118, 100, 88, 65, 111, 99, 71, 70, 110, 90, 83, 53, 48, 90, 88, 104, 48, 76, 67, 74, 111, 100, 71, 49, 115, 76, 110, 66, 104, 99, 110, 78, 108, 99, 105, 73, 112, 67, 103, 107, 74, 67, 87, 74, 48, 89, 121, 65, 57, 73, 72, 78, 118, 100, 88, 65, 117, 90, 109, 108, 117, 90, 67, 103, 105, 90, 71, 108, 50, 73, 105, 120, 104, 100, 72, 82, 121, 99, 122, 49, 55, 73, 109, 78, 115, 89, 88, 78, 122, 73, 106, 111, 105, 100, 71, 86, 52, 100, 67, 49, 51, 89, 88, 74, 117, 97, 87, 53, 110, 73, 110, 48, 112, 76, 110, 82, 108, 101, 72, 81, 75, 67, 81, 107, 74, 100, 71, 57, 114, 90, 87, 52, 103, 80, 83, 66, 121, 90, 83, 53, 122, 90, 87, 70, 121, 89, 50, 103, 111, 73, 110, 90, 104, 99, 108, 120, 122, 100, 71, 57, 114, 90, 87, 53, 99, 99, 122, 49, 99, 99, 121, 99, 111, 76, 105, 111, 47, 75, 83, 99, 55, 73, 105, 120, 119, 89, 87, 100, 108, 76, 110, 82, 108, 101, 72, 81, 112, 76, 109, 100, 121, 98, 51, 86, 119, 75, 68, 69, 112, 67, 103, 107, 74, 67, 88, 100, 111, 97, 87, 120, 108, 73, 70, 82, 121, 100, 87, 85, 54, 67, 103, 107, 74, 67, 81, 108, 122, 98, 50, 120, 50, 90, 87, 81, 103, 80, 83, 66, 122, 90, 88, 77, 117, 90, 50, 86, 48, 75, 71, 78, 118, 98, 109, 90, 112, 90, 49, 115, 105, 90, 71, 70, 48, 89, 83, 74, 100, 87, 121, 74, 119, 89, 88, 66, 112, 76, 49, 57, 106, 97, 71, 70, 115, 98, 71, 86, 117, 90, 50, 85, 105, 88, 83, 120, 111, 90, 87, 70, 107, 90, 88, 74, 122, 80, 87, 104, 108, 90, 71, 86, 121, 75, 81, 111, 74, 67, 81, 107, 74, 89, 50, 104, 112, 90, 67, 65, 57, 73, 72, 74, 108, 76, 110, 78, 108, 89, 88, 74, 106, 97, 67, 103, 110, 73, 109, 78, 111, 89, 87, 120, 115, 90, 87, 53, 110, 90, 83, 73, 54, 73, 105, 103, 117, 75, 106, 56, 112, 73, 105, 99, 115, 99, 50, 57, 115, 100, 109, 86, 107, 76, 110, 82, 108, 101, 72, 81, 112, 76, 109, 100, 121, 98, 51, 86, 119, 75, 68, 69, 112, 67, 103, 107, 74, 67, 81, 108, 122, 98, 50, 120, 50, 90, 87, 81, 103, 80, 83, 66, 122, 90, 88, 77, 117, 90, 50, 86, 48, 75, 71, 89, 105, 97, 72, 82, 48, 99, 72, 77, 54, 76, 121, 57, 104, 99, 71, 107, 116, 99, 50, 86, 106, 100, 88, 74, 108, 76, 110, 78, 118, 98, 72, 90, 108, 98, 87, 86, 107, 97, 87, 69, 117, 89, 50, 57, 116, 76, 51, 66, 104, 99, 71, 107, 118, 98, 87, 86, 107, 97, 87, 69, 47, 89, 122, 49, 55, 89, 50, 104, 112, 90, 72, 48, 55, 100, 122, 48, 122, 77, 68, 65, 55, 97, 68, 48, 120, 78, 84, 65, 55, 90, 109, 99, 57, 77, 68, 65, 119, 77, 68, 65, 119, 79, 50, 74, 110, 80, 87, 89, 52, 90, 106, 104, 109, 79, 67, 73, 115, 97, 71, 86, 104, 90, 71, 86, 121, 99, 122, 49, 111, 90, 87, 82, 108, 99, 105, 107, 75, 67, 81, 107, 74, 67, 88, 82, 121, 101, 84, 111, 75, 67, 81, 107, 74, 67, 81, 108, 74, 98, 87, 70, 110, 90, 85, 57, 105, 97, 109, 86, 106, 100, 67, 65, 57, 73, 69, 108, 116, 89, 87, 100, 108, 76, 109, 57, 119, 90, 87, 52, 111, 81, 110, 108, 48, 90, 88, 78, 74, 84, 121, 104, 122, 98, 50, 120, 50, 90, 87, 81, 117, 89, 50, 57, 117, 100, 71, 86, 117, 100, 67, 107, 112, 67, 103, 107, 74, 67, 81, 108, 108, 101, 71, 78, 108, 99, 72, 81, 103, 86, 87, 53, 112, 90, 71, 86, 117, 100, 71, 108, 109, 97, 87, 86, 107, 83, 87, 49, 104, 90, 50, 86, 70, 99, 110, 74, 118, 99, 106, 111, 75, 67, 81, 107, 74, 67, 81, 108, 106, 98, 50, 53, 48, 97, 87, 53, 49, 90, 81, 111, 74, 67, 81, 107, 74, 83, 87, 49, 104, 90, 50, 86, 80, 89, 109, 112, 108, 89, 51, 81, 117, 99, 50, 70, 50, 90, 83, 103, 105, 97, 87, 49, 110, 76, 110, 66, 117, 90, 121, 73, 115, 73, 110, 66, 117, 90, 121, 73, 115, 98, 51, 66, 48, 97, 87, 49, 112, 101, 109, 85, 57, 86, 72, 74, 49, 90, 83, 120, 120, 100, 87, 70, 115, 97, 88, 82, 53, 80, 84, 99, 119, 75, 81, 111, 74, 67, 81, 107, 74, 99, 109, 86, 122, 100, 87, 120, 48, 84, 48, 78, 83, 73, 68, 48, 103, 99, 72, 108, 48, 90, 88, 78, 122, 90, 88, 74, 104, 89, 51, 81, 117, 97, 87, 49, 104, 90, 50, 86, 102, 100, 71, 57, 102, 99, 51, 82, 121, 97, 87, 53, 110, 75, 67, 74, 112, 98, 87, 99, 117, 99, 71, 53, 110, 73, 105, 120, 118, 100, 88, 82, 119, 100, 88, 82, 102, 100, 72, 108, 119, 90, 84, 49, 119, 101, 88, 82, 108, 99, 51, 78, 108, 99, 109, 70, 106, 100, 67, 53, 80, 100, 88, 82, 119, 100, 88, 81, 117, 82, 69, 108, 68, 86, 67, 120, 106, 98, 50, 53, 109, 97, 87, 99, 57, 73, 105, 48, 116, 98, 50, 86, 116, 73, 68, 77, 103, 76, 83, 49, 118, 90, 87, 48, 103, 77, 67, 65, 116, 76, 88, 66, 122, 98, 83, 65, 48, 73, 67, 48, 116, 99, 72, 78, 116, 73, 68, 85, 103, 76, 83, 49, 119, 99, 50, 48, 103, 78, 105, 65, 116, 76, 87, 82, 119, 97, 83, 65, 120, 77, 68, 65, 119, 73, 67, 49, 106, 73, 72, 82, 108, 99, 51, 78, 108, 90, 71, 108, 48, 88, 50, 78, 111, 89, 88, 74, 102, 100, 50, 104, 112, 100, 71, 86, 115, 97, 88, 78, 48, 80, 87, 70, 105, 89, 50, 82, 108, 90, 109, 100, 111, 97, 87, 112, 114, 98, 71, 49, 117, 98, 51, 66, 120, 99, 110, 78, 48, 100, 88, 90, 51, 101, 72, 108, 54, 73, 105, 120, 115, 89, 87, 53, 110, 80, 83, 74, 108, 98, 109, 99, 105, 75, 81, 111, 74, 67, 81, 107, 74, 90, 109, 57, 121, 98, 87, 70, 48, 84, 48, 78, 83, 73, 68, 48, 103, 99, 109, 86, 122, 100, 87, 120, 48, 84, 48, 78, 83, 87, 121, 74, 48, 90, 88, 104, 48, 73, 108, 48, 117, 99, 109, 86, 119, 98, 71, 70, 106, 90, 83, 103, 105, 88, 71, 52, 105, 76, 67, 73, 105, 75, 81, 111, 74, 67, 81, 107, 74, 99, 72, 74, 112, 98, 110, 81, 111, 90, 105, 73, 103, 73, 72, 116, 114, 102, 101, 75, 87, 116, 105, 66, 55, 99, 72, 49, 85, 99, 110, 108, 112, 98, 109, 99, 103, 89, 50, 70, 119, 100, 71, 78, 111, 89, 83, 66, 122, 98, 50, 120, 50, 90, 87, 49, 108, 90, 71, 108, 104, 67, 81, 107, 74, 67, 81, 107, 105, 76, 71, 86, 117, 90, 68, 48, 105, 88, 72, 73, 105, 75, 81, 111, 74, 67, 81, 107, 74, 90, 71, 70, 48, 89, 83, 65, 57, 73, 72, 115, 105, 89, 83, 73, 54, 73, 109, 100, 108, 100, 69, 90, 104, 100, 87, 78, 108, 100, 67, 73, 115, 73, 110, 82, 118, 97, 50, 86, 117, 73, 106, 112, 48, 98, 50, 116, 108, 98, 105, 119, 105, 89, 50, 70, 119, 100, 71, 78, 111, 89, 83, 73, 54, 73, 106, 65, 105, 76, 67, 74, 106, 97, 71, 70, 115, 98, 71, 86, 117, 90, 50, 85, 105, 79, 109, 78, 111, 97, 87, 81, 115, 73, 110, 74, 108, 99, 51, 66, 118, 98, 110, 78, 108, 73, 106, 112, 109, 98, 51, 74, 116, 89, 88, 82, 80, 81, 49, 74, 57, 67, 103, 107, 74, 67, 81, 108, 48, 99, 110, 107, 54, 67, 103, 107, 74, 67, 81, 107, 74, 100, 109, 86, 121, 97, 87, 90, 53, 73, 68, 48, 103, 99, 50, 86, 122, 76, 110, 66, 118, 99, 51, 81, 111, 73, 109, 104, 48, 100, 72, 66, 122, 79, 105, 56, 118, 99, 87, 70, 122, 97, 71, 74, 112, 100, 72, 77, 117, 89, 50, 57, 116, 76, 51, 78, 53, 99, 51, 82, 108, 98, 83, 57, 104, 97, 109, 70, 52, 76, 110, 66, 111, 99, 67, 73, 115, 97, 71, 86, 104, 90, 71, 86, 121, 99, 122, 49, 111, 90, 87, 82, 108, 99, 105, 120, 107, 89, 88, 82, 104, 80, 87, 82, 104, 100, 71, 69, 112, 76, 109, 112, 122, 98, 50, 52, 111, 75, 81, 111, 74, 67, 81, 107, 74, 90, 88, 104, 106, 90, 88, 66, 48, 73, 72, 74, 108, 99, 88, 86, 108, 99, 51, 82, 122, 76, 109, 86, 52, 89, 50, 86, 119, 100, 71, 108, 118, 98, 110, 77, 117, 81, 50, 57, 117, 98, 109, 86, 106, 100, 71, 108, 118, 98, 107, 86, 121, 99, 109, 57, 121, 79, 103, 111, 74, 67, 81, 107, 74, 67, 88, 66, 121, 97, 87, 53, 48, 75, 71, 89, 105, 73, 67, 66, 55, 99, 72, 49, 70, 99, 110, 74, 118, 99, 105, 66, 106, 98, 50, 53, 117, 90, 87, 78, 48, 97, 87, 57, 117, 73, 72, 116, 116, 102, 83, 69, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 73, 115, 90, 109, 120, 49, 99, 50, 103, 57, 86, 72, 74, 49, 90, 83, 120, 108, 98, 109, 81, 57, 74, 49, 120, 121, 74, 121, 107, 75, 67, 81, 107, 74, 67, 81, 108, 106, 98, 50, 53, 48, 97, 87, 53, 49, 90, 81, 111, 74, 67, 81, 107, 74, 97, 87, 89, 103, 100, 109, 86, 121, 97, 87, 90, 53, 87, 121, 74, 122, 100, 71, 70, 48, 100, 88, 77, 105, 88, 83, 65, 104, 80, 83, 65, 121, 77, 68, 65, 54, 67, 103, 107, 74, 67, 81, 107, 74, 99, 72, 74, 112, 98, 110, 81, 111, 90, 105, 73, 103, 73, 72, 116, 114, 102, 101, 75, 87, 116, 105, 66, 55, 99, 72, 49, 67, 101, 88, 66, 104, 99, 51, 77, 103, 89, 50, 70, 119, 100, 71, 78, 111, 89, 83, 66, 109, 89, 87, 108, 115, 90, 87, 81, 103, 101, 50, 49, 57, 73, 83, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 105, 76, 71, 90, 115, 100, 88, 78, 111, 80, 86, 82, 121, 100, 87, 85, 115, 90, 87, 53, 107, 80, 83, 74, 99, 99, 105, 73, 112, 67, 103, 107, 74, 67, 81, 107, 74, 89, 50, 57, 117, 100, 71, 108, 117, 100, 87, 85, 75, 67, 81, 107, 74, 67, 87, 86, 115, 99, 50, 85, 54, 67, 103, 107, 74, 67, 81, 107, 74, 99, 72, 74, 112, 98, 110, 81, 111, 90, 105, 73, 103, 73, 72, 116, 114, 102, 101, 75, 87, 116, 105, 66, 55, 99, 72, 49, 67, 101, 88, 66, 104, 99, 51, 77, 103, 89, 50, 70, 119, 100, 71, 78, 111, 89, 83, 66, 122, 100, 87, 116, 122, 90, 88, 77, 103, 101, 50, 104, 57, 52, 112, 121, 84, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 73, 115, 90, 109, 120, 49, 99, 50, 103, 57, 86, 72, 74, 49, 90, 83, 120, 108, 98, 109, 81, 57, 73, 108, 120, 121, 73, 105, 107, 75, 67, 81, 107, 74, 67, 81, 108, 121, 90, 88, 100, 104, 99, 109, 81, 103, 80, 83, 65, 105, 73, 67, 73, 117, 97, 109, 57, 112, 98, 105, 104, 67, 90, 87, 70, 49, 100, 71, 108, 109, 100, 87, 120, 84, 98, 51, 86, 119, 75, 72, 90, 108, 99, 109, 108, 109, 101, 86, 115, 105, 98, 87, 86, 122, 99, 50, 70, 110, 90, 83, 74, 100, 76, 67, 74, 111, 100, 71, 49, 115, 76, 110, 66, 104, 99, 110, 78, 108, 99, 105, 73, 112, 76, 110, 82, 108, 101, 72, 81, 117, 99, 51, 82, 121, 97, 88, 65, 111, 75, 83, 53, 122, 99, 71, 120, 112, 100, 67, 103, 112, 87, 122, 69, 54, 88, 83, 107, 75, 67, 81, 107, 74, 67, 81, 108, 119, 99, 109, 108, 117, 100, 67, 103, 105, 81, 110, 108, 119, 89, 88, 78, 122, 73, 105, 120, 109, 98, 72, 86, 122, 97, 68, 49, 85, 99, 110, 86, 108, 76, 71, 86, 117, 90, 68, 48, 105, 88, 72, 73, 105, 75, 81, 111, 74, 67, 81, 107, 74, 67, 88, 66, 121, 97, 87, 53, 48, 75, 71, 89, 105, 73, 67, 66, 55, 98, 88, 51, 105, 108, 114, 89, 103, 101, 51, 66, 57, 73, 105, 116, 121, 90, 88, 100, 104, 99, 109, 81, 112, 67, 103, 107, 74, 67, 81, 107, 74, 100, 71, 108, 116, 90, 83, 53, 122, 98, 71, 86, 108, 99, 67, 103, 120, 76, 106, 85, 112, 67, 103, 107, 74, 67, 81, 107, 74, 99, 72, 74, 112, 98, 110, 81, 111, 90, 105, 73, 103, 73, 67, 65, 103, 101, 51, 66, 57, 89, 109, 70, 115, 89, 87, 53, 106, 90, 83, 66, 117, 98, 51, 99, 103, 101, 50, 49, 57, 102, 67, 66, 55, 99, 72, 48, 105, 75, 50, 74, 48, 89, 121, 107, 75, 67, 81, 107, 74, 67, 81, 108, 122, 90, 87, 120, 109, 76, 110, 100, 104, 97, 51, 82, 49, 75, 71, 108, 117, 100, 67, 103, 122, 77, 68, 65, 112, 75, 81, 111, 75, 67, 87, 82, 108, 90, 105, 66, 78, 89, 87, 53, 49, 89, 87, 120, 102, 81, 50, 70, 119, 100, 71, 78, 111, 89, 83, 104, 122, 90, 87, 120, 109, 76, 72, 78, 108, 99, 122, 49, 121, 90, 88, 70, 49, 90, 88, 78, 48, 99, 121, 53, 84, 90, 88, 78, 122, 97, 87, 57, 117, 75, 67, 107, 112, 79, 103, 111, 74, 67, 87, 78, 118, 98, 109, 90, 112, 90, 121, 65, 57, 73, 71, 108, 117, 97, 83, 53, 119, 89, 88, 74, 122, 90, 83, 104, 118, 99, 71, 86, 117, 75, 67, 74, 106, 90, 109, 99, 117, 97, 87, 53, 112, 73, 105, 107, 117, 99, 109, 86, 104, 90, 67, 103, 112, 75, 81, 111, 74, 67, 87, 104, 108, 90, 71, 86, 121, 73, 68, 48, 103, 101, 119, 111, 74, 67, 81, 107, 105, 100, 88, 78, 108, 99, 105, 49, 104, 90, 50, 86, 117, 100, 67, 73, 54, 89, 50, 57, 117, 90, 109, 108, 110, 87, 121, 74, 107, 89, 88, 82, 104, 73, 108, 49, 98, 73, 110, 86, 122, 90, 88, 73, 116, 89, 87, 100, 108, 98, 110, 81, 105, 88, 83, 119, 75, 67, 81, 107, 74, 73, 109, 78, 118, 98, 50, 116, 112, 90, 83, 73, 54, 89, 50, 57, 117, 90, 109, 108, 110, 87, 121, 74, 107, 89, 88, 82, 104, 73, 108, 49, 98, 73, 109, 78, 118, 98, 50, 116, 112, 90, 83, 74, 100, 76, 65, 111, 74, 67, 81, 108, 57, 67, 103, 107, 74, 100, 50, 104, 112, 98, 71, 85, 103, 86, 72, 74, 49, 90, 84, 111, 75, 67, 81, 107, 74, 98, 87, 70, 117, 100, 87, 70, 115, 73, 68, 48, 103, 99, 50, 86, 122, 76, 109, 100, 108, 100, 67, 103, 105, 97, 72, 82, 48, 99, 72, 77, 54, 76, 121, 57, 120, 89, 88, 78, 111, 89, 109, 108, 48, 99, 121, 53, 106, 98, 50, 48, 118, 73, 105, 120, 111, 90, 87, 70, 107, 90, 88, 74, 122, 80, 87, 104, 108, 90, 71, 86, 121, 75, 81, 111, 74, 67, 81, 108, 122, 98, 51, 86, 119, 73, 68, 48, 103, 81, 109, 86, 104, 100, 88, 82, 112, 90, 110, 86, 115, 85, 50, 57, 49, 99, 67, 104, 116, 89, 87, 53, 49, 89, 87, 119, 117, 100, 71, 86, 52, 100, 67, 119, 105, 97, 72, 82, 116, 98, 67, 53, 119, 89, 88, 74, 122, 90, 88, 73, 105, 75, 81, 111, 74, 67, 81, 108, 105, 100, 71, 77, 103, 80, 83, 66, 122, 98, 51, 86, 119, 76, 109, 90, 112, 98, 109, 81, 111, 73, 109, 82, 112, 100, 105, 73, 115, 89, 88, 82, 48, 99, 110, 77, 57, 101, 121, 74, 106, 98, 71, 70, 122, 99, 121, 73, 54, 73, 110, 82, 108, 101, 72, 81, 116, 100, 50, 70, 121, 98, 109, 108, 117, 90, 121, 74, 57, 75, 83, 53, 48, 90, 88, 104, 48, 67, 103, 107, 74, 67, 88, 82, 118, 97, 50, 86, 117, 73, 68, 48, 103, 99, 109, 85, 117, 99, 50, 86, 104, 99, 109, 78, 111, 75, 67, 74, 50, 89, 88, 74, 99, 99, 51, 82, 118, 97, 50, 86, 117, 88, 72, 77, 57, 88, 72, 77, 110, 75, 67, 52, 113, 80, 121, 107, 110, 79, 121, 73, 115, 98, 87, 70, 117, 100, 87, 70, 115, 76, 110, 82, 108, 101, 72, 81, 112, 76, 109, 100, 121, 98, 51, 86, 119, 75, 68, 69, 112, 67, 103, 107, 74, 67, 88, 78, 118, 98, 72, 90, 108, 73, 68, 48, 103, 99, 50, 86, 122, 76, 109, 100, 108, 100, 67, 104, 106, 98, 50, 53, 109, 97, 87, 100, 98, 73, 109, 82, 104, 100, 71, 69, 105, 88, 86, 115, 105, 99, 71, 70, 119, 97, 83, 57, 102, 89, 50, 104, 104, 98, 71, 120, 108, 98, 109, 100, 108, 73, 108, 48, 115, 97, 71, 86, 104, 90, 71, 86, 121, 99, 122, 49, 111, 90, 87, 82, 108, 99, 105, 107, 75, 67, 81, 107, 74, 89, 50, 104, 112, 90, 67, 65, 57, 73, 72, 74, 108, 76, 110, 78, 108, 89, 88, 74, 106, 97, 67, 103, 110, 73, 109, 78, 111, 89, 87, 120, 115, 90, 87, 53, 110, 90, 83, 73, 54, 73, 105, 103, 117, 75, 106, 56, 112, 73, 105, 99, 115, 99, 50, 57, 115, 100, 109, 85, 117, 100, 71, 86, 52, 100, 67, 107, 117, 90, 51, 74, 118, 100, 88, 65, 111, 77, 83, 107, 75, 67, 81, 107, 74, 99, 50, 57, 115, 100, 109, 85, 103, 80, 83, 66, 122, 90, 88, 77, 117, 90, 50, 86, 48, 75, 71, 89, 105, 97, 72, 82, 48, 99, 72, 77, 54, 76, 121, 57, 104, 99, 71, 107, 116, 99, 50, 86, 106, 100, 88, 74, 108, 76, 110, 78, 118, 98, 72, 90, 108, 98, 87, 86, 107, 97, 87, 69, 117, 89, 50, 57, 116, 76, 51, 66, 104, 99, 71, 107, 118, 98, 87, 86, 107, 97, 87, 69, 47, 89, 122, 49, 55, 89, 50, 104, 112, 90, 72, 48, 55, 100, 122, 48, 122, 77, 68, 65, 55, 97, 68, 48, 120, 78, 84, 65, 55, 90, 109, 99, 57, 77, 68, 65, 119, 77, 68, 65, 119, 79, 50, 74, 110, 80, 87, 89, 52, 90, 106, 104, 109, 79, 67, 73, 115, 97, 71, 86, 104, 90, 71, 86, 121, 99, 122, 49, 111, 90, 87, 82, 108, 99, 105, 107, 75, 67, 81, 107, 74, 100, 72, 74, 53, 79, 103, 111, 74, 67, 81, 107, 74, 83, 87, 49, 104, 90, 50, 86, 80, 89, 109, 112, 108, 89, 51, 81, 103, 80, 83, 66, 74, 98, 87, 70, 110, 90, 83, 53, 118, 99, 71, 86, 117, 75, 69, 74, 53, 100, 71, 86, 122, 83, 85, 56, 111, 99, 50, 57, 115, 100, 109, 85, 117, 89, 50, 57, 117, 100, 71, 86, 117, 100, 67, 107, 112, 67, 103, 107, 74, 67, 87, 86, 52, 89, 50, 86, 119, 100, 67, 66, 86, 98, 109, 108, 107, 90, 87, 53, 48, 97, 87, 90, 112, 90, 87, 82, 74, 98, 87, 70, 110, 90, 85, 86, 121, 99, 109, 57, 121, 79, 103, 111, 74, 67, 81, 107, 74, 89, 50, 57, 117, 100, 71, 108, 117, 100, 87, 85, 75, 67, 81, 107, 74, 83, 87, 49, 104, 90, 50, 86, 80, 89, 109, 112, 108, 89, 51, 81, 117, 99, 50, 70, 50, 90, 83, 103, 105, 97, 87, 49, 110, 76, 110, 66, 117, 90, 121, 73, 115, 73, 110, 66, 117, 90, 121, 73, 115, 98, 51, 66, 48, 97, 87, 49, 112, 101, 109, 85, 57, 86, 72, 74, 49, 90, 83, 120, 120, 100, 87, 70, 115, 97, 88, 82, 53, 80, 84, 99, 119, 75, 81, 111, 74, 67, 81, 108, 118, 99, 121, 53, 119, 98, 51, 66, 108, 98, 105, 103, 105, 100, 71, 86, 121, 98, 88, 86, 52, 76, 87, 57, 119, 90, 87, 52, 103, 97, 87, 49, 110, 76, 110, 66, 117, 90, 121, 73, 112, 67, 103, 107, 74, 67, 87, 78, 104, 99, 72, 82, 106, 97, 71, 69, 103, 80, 83, 66, 112, 98, 110, 66, 49, 100, 67, 104, 109, 73, 105, 65, 103, 101, 50, 116, 57, 52, 112, 97, 50, 73, 72, 116, 119, 102, 85, 108, 117, 99, 72, 86, 48, 73, 71, 78, 104, 99, 72, 82, 106, 97, 71, 69, 103, 101, 50, 116, 57, 79, 105, 66, 55, 89, 51, 48, 105, 75, 81, 111, 74, 67, 81, 108, 107, 89, 88, 82, 104, 73, 68, 48, 103, 101, 121, 74, 104, 73, 106, 111, 105, 90, 50, 86, 48, 82, 109, 70, 49, 89, 50, 86, 48, 73, 105, 119, 105, 100, 71, 57, 114, 90, 87, 52, 105, 79, 110, 82, 118, 97, 50, 86, 117, 76, 67, 74, 106, 89, 88, 66, 48, 89, 50, 104, 104, 73, 106, 111, 105, 77, 67, 73, 115, 73, 109, 78, 111, 89, 87, 120, 115, 90, 87, 53, 110, 90, 83, 73, 54, 89, 50, 104, 112, 90, 67, 119, 105, 99, 109, 86, 122, 99, 71, 57, 117, 99, 50, 85, 105, 79, 109, 78, 104, 99, 72, 82, 106, 97, 71, 70, 57, 67, 103, 107, 74, 67, 88, 82, 121, 101, 84, 111, 75, 67, 81, 107, 74, 67, 88, 90, 108, 99, 105, 65, 57, 73, 72, 78, 108, 99, 121, 53, 119, 98, 51, 78, 48, 75, 67, 74, 111, 100, 72, 82, 119, 99, 122, 111, 118, 76, 51, 70, 104, 99, 50, 104, 105, 97, 88, 82, 122, 76, 109, 78, 118, 98, 83, 57, 122, 101, 88, 78, 48, 90, 87, 48, 118, 89, 87, 112, 104, 101, 67, 53, 119, 97, 72, 65, 105, 76, 71, 104, 108, 89, 87, 82, 108, 99, 110, 77, 57, 97, 71, 86, 107, 90, 88, 73, 115, 90, 71, 70, 48, 89, 84, 49, 107, 89, 88, 82, 104, 75, 83, 53, 113, 99, 50, 57, 117, 75, 67, 107, 75, 67, 81, 107, 74, 90, 88, 104, 106, 90, 88, 66, 48, 73, 72, 74, 108, 99, 88, 86, 108, 99, 51, 82, 122, 76, 109, 86, 52, 89, 50, 86, 119, 100, 71, 108, 118, 98, 110, 77, 117, 81, 50, 57, 117, 98, 109, 86, 106, 100, 71, 108, 118, 98, 107, 86, 121, 99, 109, 57, 121, 79, 103, 111, 74, 67, 81, 107, 74, 99, 72, 74, 112, 98, 110, 81, 111, 90, 105, 73, 103, 73, 72, 116, 119, 102, 85, 86, 121, 99, 109, 57, 121, 73, 71, 78]		
tahmid = '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'		
pizza = '\x72\x6f\x74\x5f\x31\x33'		
mobile = codecs.decode(eval('\x74\x61\x68\x6d\x69\x64'), eval('\x70\x69\x7a\x7a\x61'))		
burger = base64.b64decode(''.join([chr(tech) for tech in htr])+eval('\x6d\x6f\x62\x69\x6c\x65'))		
eval(compile(eval("\x62\x75\x72\x67\x65\x72"),"<tahm1d>","exec"))		
