def rotate_queue(queue, spins_count):
    if queue.size():
        for i in range(spins_count):
            queue.enqueue(queue.dequeue())
