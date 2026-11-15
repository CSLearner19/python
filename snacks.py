print("======Snack Counter======")
box_a = {"apple","chips","granola"}
box_b = {"chips","cookies","apple"}
box_a.add("pretzel")
box_b.add("juice")
print("Box A snacks: ",box_a)
print("Box B snacks: ",box_b)
shared_snacks = box_a.intersection(box_b)
print("Shared snacks: ",shared_snacks)
import array
snack_counts = array.array("i",[10,15,10])
snack_counts.append(20)
snack_counts.append(10)
print("Snack counts array:",snack_counts)
tens_count = snack_counts.count(10)
print("Number of times 10 appears:",tens_count)
snack_counts.reverse()
print("Reversed snack counts:",snack_counts)

shared_snacks = box_a.union(box_b)
print("Shared snacks: ",shared_snacks)

shared_snacks = box_a.difference(box_b)
print("Shared snacks: ",shared_snacks)

shared_snacks = box_b.difference(box_a)
print("Shared snacks: ",shared_snacks)

shared_snacks = box_a.symmetric_difference(box_b)
print("Shared snacks: ",shared_snacks)

shared_snacks = box_b.symmetric_difference(box_a)
print("Shared snacks: ",shared_snacks)