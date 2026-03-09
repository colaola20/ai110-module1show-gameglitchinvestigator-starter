# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  - The difficulty levels aren't applying. When I start an easy round which should pick a number from a range 1 to 20, it picks from 1 to 100 and lower the number of attempts, making the game more complicated than before. Similar thing with hard round where range suppose to be 1 to 50 with 4 attemots, but range stays the same - 1 to 100.
 
  - The game don't provide correct feedback to a player, specifying always the opposite direction "Go lower." instead of "Go higher.".

  - The New Game button isn't starting a new game after a player has finished the round.

  - The round discription doesn't correspond to the round settings. For example, for normal round, the description says that player has 8 attemps while in reality only 7.

  - Secret always in range from 1 to 100 no matter what difficulty level is
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
- Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Claude sugested to switch feedback messages when checking if guess > secret which fixed the hint's error. I verified it by playing the game.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
