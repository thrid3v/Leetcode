class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        emp_times = collections.defaultdict(list)

        for name, time_str in zip(keyName, keyTime):
            hours, minutes = map(int, time_str.split(':'))
            total_minutes = hours * 60 + minutes
            emp_times[name].append(total_minutes)
        
        emps = set()

        for name, times in emp_times.items():
            times.sort()

            for i in range(len(times)-2):
                if times[i+2] - times[i] <= 60:
                    emps.add(name)
                    break 
        
        return sorted(list(emps))
        