# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
- 1. I noticed that the score total was not properly set so I expect that the final total would not be computed correctly.
- 2. I noticed that the "New Game" button didn't work properly so I expect that the game wouldn't end.

- 3. One specific glitch I found is the messages being printed in the check_guess function. I asked AI to explain the logic behind it and how it led to generating faulty outputs.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Copilot and some Claude Code.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One example was the separation of concerns when moving the logic from app.py to logic_utils.py

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result)

The logic with the user's guesses and going beyond the range of a given difficulty.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

Did by first looking at the code for logic clarity and then ran the game to see if there was any broken logic that was not leading to 
errors like the secret not changing when selecting difficulties.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran a test for a wining guess using both methods and what it showed was a small part of the method was flawed which I used copliot to get to the root cause.

- Did AI help you design or understand any tests? How?
It helped me design edge case tests to make sure it was fully functional.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

It was changing because of the streamlit script running from top to bottom so code positioning was crucial for functionality. 

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns is like a mainframe where there is a proper way to start and run it, like when a user is interacting with the application. 

- What change did you make that finally gave the game a stable secret number?

I moved the logic to the bottom so that the number updates before any other interactivity occurred.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Testing my code and practicing separation of concerns as well as prompting the model to get more from it.

- What is one thing you would do differently next time you work with AI on a coding task?

Probably explaining more with regards to the context of a specific component im having trouble with.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This changed the way I have to design my prompts as well as proofreading the reponses from the model.