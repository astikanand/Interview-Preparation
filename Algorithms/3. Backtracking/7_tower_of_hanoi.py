def tower_of_hanoi(n, source, auxiliary, destination):
    if(n>0):
        # Move n-1 disks from source to auxilliary using destination
        tower_of_hanoi(n-1, source, destination, auxiliary)

        # Move that 1 disk now from source to destination
        print("Move 1 disk from {} to {}".format(source, destination))

        # Move rest n-1 from auxiliary to destination using source
        tower_of_hanoi(n-1, auxiliary, source, destination)



print("Tower of Hanoi Example-1")
tower_of_hanoi(3, "A", "B", "C")

print("\nTower of Hanoi Example-2")
tower_of_hanoi(4, "A", "B", "C")
