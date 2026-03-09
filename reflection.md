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

  - Secret always in range from 1 to 100 no matter what difficulty level is.

  - Score calculation is off.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
- Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - Claude sugested to switch feedback messages when checking if guess > secret which fixed the hint's error. I verified it by playing the game.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - I want input fiels to clear every time the new game starts, so AI recommended to set st.session_state[f"guess_input_{difficulty}"] to an empty string which led to a new error: `st.session_state.guess_input_Normal` cannot be modified after the widget with key `guess_input_Normal` is instantiated. After AI suggested few others things which didn't work.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - Most of the time I checked myself by testing website but eventually I used pytest with test cases I had and i also ask AI to generate some more cases. All test cases in tests/test_game_logic.py passed.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - I test 'New Game" button manually on the website when the game has started yes, when the game is playing, and finally when it's finished. I also asked AI to generate pytest cases and than I run them too.

- Did AI help you design or understand any tests? How?
  - Yes, AI helped me designed test cases for "New Game" button. I wnated all games start with an empty text field an dit was a little tricky.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
   - To be honest I haven't noticed this one in particular :)

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Rerun command stops the current script and reruns it staring from top to the button, so the app reinitializes every time and session state dictionary is the only thing which preserves in this process.
- What change did you make that finally gave the game a stable secret number?
  - None, my secret number was always stable.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    - I really, liked refactoring game logic and moving it to a separate logic_utils.py file. It helped me to debug and process the code faster and easier. I definatly will be using   it in the future. I also like using pytest since it can safe a lot of time and help thoroughly test the app.

- What is one thing you would do differently next time you work with AI on a coding task?
  - To be honest I'm sure. This experience was a really good one. I think it was very efficient to break tasks down into small parts, using specific prompts, and always start with a new chat. It was smooth experience.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - This thought is not new to me but it always true: Always make sure the changes work. Test, test, and again test.
