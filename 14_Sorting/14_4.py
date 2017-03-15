procedure render_a_calendar(list_of_events):
--------------------------------------------
	- num_simulataneous_events = 0
	- max_simultaneous_events = -inf
	- endpoints = Sort end points according to time; breaking ties by giving start time priority over end 	time
	for point in endpoints:
		- if point is start:
			- num_simultaneous_events++
			- max_simultaneous_events = max(max_simultaneous_events, num_simultaneous_events)
		- else:
			- num_simultaneous_events--
	- return max_simultaneous_events