def create_counter(number):

	current_count = number

	def up():
		nonlocal current_count
		current_count += 1
		return current_count
	
	def down():
		nonlocal current_count
		current_count -= 1
		return current_count

	return {'up': up, 'down': down}
