Sliding Window: Longest Unique Substring
Goal: longest substring with no repeating chars.

Core idea:
scan right → fix left → update best
	•	left = window start
	•	right = window end
	•	best = max(best, right-left+1)

Version A: seen set (with while)
	•	seen holds chars currently in the window.
	•	If ch repeats: shrink from left until ch is not in seen.
	•	Key line:
	•	while ch in seen: seen.remove(s[left]); left += 1

Why remove s[left]?
Because we shrink the window from the left side.

Version B: last dict (no while)
	•	last[ch] = last index where ch appeared.
	•	If ch repeats inside current window: jump left.
	•	Key line:
	•	left = max(left, last[ch] + 1)

Common bug traps
	•	counting frequencies globally doesn’t work (problem is local window).
	•	best is not best += 1; it must use right-left+1.
	•	use +1 because indices are inclusive.

****

•	“Hard part: remembering that while ch in seen means we must remove s[left] (not ch).”
•    “Hard
part: best = max(best, right - left + 1)(window
length).”