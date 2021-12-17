def f(s) -> int:
	d = Counter(list(s))
	r = 0
	t = {}
	for i in range(len(s)):
		t[s[i]] = t.get(s[i], 0) + 1
		d[s[i]] -= 1
		if d[s[i]] == 0:
			d.pop(s[i])
		if len(t) == len(d):
			r += 1
		elif len(t) > len(d):
			break
	return r
