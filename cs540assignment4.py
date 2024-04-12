# Function for LRU Algorithm
def lru_algorithm(reference_string, size):
    # List to store pages currently in memory
    pages = []
    # Counter for page faults
    faults = 0
    # Counter for page hits
    hits = 0

    # Iterate through each page in the reference string
    for ref_page in reference_string:
        # Check if the page is already in memory
        if ref_page in pages:
            # If yes, remove it and append it to the end (LRU)
            pages.remove(ref_page)
            pages.append(ref_page)
            # Increment the page hit counter
            hits += 1
        else:
            # If the page is not in memory, it's a page fault
            faults += 1
            # If memory is not full, add the page to memory
            if len(pages) < size:
                pages.append(ref_page)
            else:
                # If memory is full, remove the least recently used page (first in the list)
                pages.pop(0)
                # Add the new page to memory
                pages.append(ref_page)
        # Print the current step, page fault, page table, frames, and faults
        print(f"Step {len(pages)}: Page fault ({ref_page}) - Page Table: {set(pages)}, Frames: {pages}, Faults: {faults}")

    return faults

# Function for FIFO Algorithm
def fifo_algorithm(reference_string, size):
    # List to store pages currently in memory
    pages = []
    # Counter for page faults
    faults = 0

    # Iterate through each page in the reference string
    for ref_page in reference_string:
        # Check if the page is not in memory (page fault)
        if ref_page not in pages:
            # Increment the page fault counter
            faults += 1
            # If memory is not full, add the page to memory
            if len(pages) < size:
                pages.append(ref_page)
            else:
                # If memory is full, remove the oldest page (first in the list)
                pages.pop(0)
                # Add the new page to memory
                pages.append(ref_page)
        # Print the current step, page fault, page table, frames, and faults
        print(f"Step {len(pages)}: Page fault ({ref_page}) - Page Table: {set(pages)}, Frames: {pages}, Faults: {faults}")

    return faults

# Function for Optimal Algorithm
def opt_algorithm(reference_string, size):
    # List to store pages currently in memory
    pages = []
    # Counter for page faults
    faults = 0

    # Iterate through each page index and page in the reference string
    for i, ref_page in enumerate(reference_string):
        # Check if the page is not in memory (page fault)
        if ref_page not in pages:
            # Increment the page fault counter
            faults += 1
            # If memory is not full, add the page to memory
            if len(pages) < size:
                pages.append(ref_page)
            else:
                # Find the optimal page to replace (furthest page in the future)
                optimal_page = max((index for index, p in enumerate(reference_string[i+1:]) if p in pages), default=-1)
                if optimal_page != -1:
                    # Remove the optimal page from memory
                    pages.remove(reference_string[i+1+optimal_page])
                    # Add the new page to memory
                    pages.append(ref_page)
        # Print the current step, page fault, page table, frames, and faults
        print(f"Step {len(pages)}: Page fault ({ref_page}) - Page Table: {set(pages)}, Frames: {pages}, Faults: {faults}")

    return faults

# Sample Input
reference_string = [1, 2, 1, 0, 3, 0, 4, 2, 4]
num_frames = 3

# Simulate LRU
print("For LRU Algorithm:")
lru_faults = lru_algorithm(reference_string, num_frames)
print(f"Total Page Faults: {lru_faults}\n")

# Simulate FIFO
print("For FIFO Algorithm:")
fifo_faults = fifo_algorithm(reference_string, num_frames)
print(f"Total Page Faults: {fifo_faults}\n")

# Simulate Optimal
print("For Optimal Algorithm:")
optimal_faults = opt_algorithm(reference_string, num_frames)
print(f"Total Page Faults: {optimal_faults}")


