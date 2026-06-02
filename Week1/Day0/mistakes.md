# Mistakes & Lessons Learned

## Mistake 1

Tried:

```powershell
mkdir SummerAnalytics2026/Week1/{Day0,Day1,Day2,Day3,Day4,Day5}
```

Expected:

Multiple folders creation.

Issue:

PowerShell does not support Bash brace expansion.

Solution:

Use:

```powershell
'Day0'..'Day5' | ForEach-Object {
    mkdir $_
}
```

---

## Mistake 2

Created temporary functions in terminal.

Issue:

Functions disappeared after closing PowerShell.

Solution:

Store them inside:

```powershell
$PROFILE
```

---

## Mistake 3

Using Linux examples directly in PowerShell.

Lesson:

Always verify whether a command is:

* Bash
* CMD
* PowerShell

before using it.
