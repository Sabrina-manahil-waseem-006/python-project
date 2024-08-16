
# <div align="center">  🎓 Title: Learning Play Zone 🎓 </div>

# 📊 Project Overview:
This project, developed as part of my first-semester coursework, is a responsive and fully functional desktop application aimed at enhancing and improving the learning skills of children. The application provides an interactive and educational experience where kids are encouraged to engage with visual content to reinforce their learning.

---
# ❓ Problem statement:
Crafting a Special Learning Experience for Little Ones
In the world of early childhood education, we set out to create something unique—a Python-based 
learning app tailor-made for preschoolers aged 3 to 5. Our aim was simple yet profound: to provide an 
engaging and educational journey focused on the joy of identifying pictures.

---
# ⭐ Key Features:
_User-Friendly Interface_:<br>
The application features a simple and intuitive user interface designed to be accessible and easy to navigate for young children.<br>

_Interactive Learning_:<br>
Children are presented with a series of images and asked to inspect them carefully. They then select the correct option from multiple choices, helping them to learn through visual association and critical thinking.<br>

_Responsive Design_:<br>
The application is built to be fully responsive, ensuring a consistent and seamless experience across different screen sizes and resolutions.<br>

_Educational Focus_:<br>
The app is designed with an educational purpose, aiming to improve children's observational skills, decision-making, and knowledge retention through an engaging and interactive approach.<br>

Performance and Stability:<br>
As a fully functional application, it has been rigorously tested to ensure smooth performance and stability, providing a reliable learning tool for kids.<br>

---

# ✨ Distinctive Elements of the Application:

💾 Database Connection:<br> 
The code establishes a connection to a Microsoft Access database using 
the pyodbc library. It uses the global variable p to inserts the player's score into the 'score' table 
and retrieves the latest score from the database.

🖥️ GUI Components:  
The GUI is built using Tkinter. Canvas is used to create a drawable area for 
placing various GUI components. Labels are used to display messages, images, and headings. 
Radiobuttons are used for the multiple-choice options for identifying the image. Buttons are 
included for navigation and submitting answers.

🖼️ Image Handling: <br> 
The script loads and displays images (e.g., apple, ice cream, swing, etc.) to 
represent questions. The images are displayed using the Tkinter PhotoImage class.

🎯 Score Tracking: <br> 
The global variable p is used to track the kid's score. Functions like correct() 
and wrong() update the score and display corresponding messages based on the kid's response.

🧩 Question Flow:<br> 
The questions follows a linear flow, with each question displayed one at a time.
For each question, the user can choose from multiple options using Radiobuttons. After 
answering a question, the user can navigate to the next or previous question.

🗨️ Feedback Messages: <br> 
The script provides feedback messages (e.g., "WELLDONE!" or "OOPS! 
WRONG ANSWER") based on the user's response to each question.

📁 File Paths:  
The script includes file paths for loading images from the local file system.

🔢 IntVar for Radiobuttons: <br> 
The IntVar named selected_option is used to keep track of the user's 
selected option among the Radiobuttons

---
# 🖼️ Screenshots of main features:  

✔️ upon clicking the play button main window appears
<br><br>
![Alt text](https://github.com/Sabrina-manahil-waseem-006/python-project/blob/main/1.JPG)
<br><br>
✔️ Upon clicking the button of right option, ‘OOPS! WRONG ANSWER’ message displays
<br><br>
![Alt text](https://github.com/Sabrina-manahil-waseem-006/python-project/blob/main/2.JPG)
<br><br>
✔️ Upon clicking the button of right option, ‘WELLDONE’ message displays
<br><br>
![Alt text](https://github.com/Sabrina-manahil-waseem-006/python-project/blob/main/3.JPG)
<br><br>
✔️Upon pressing the 'Next' button, the display will advance to the next page. Similarly, pressing the 
'Previous' button will show the previous page.
<br><br>
![Alt text](https://github.com/Sabrina-manahil-waseem-006/python-project/blob/main/4.JPG)
<br><br>
✔️ On the last image there is an option of viewing total score
<br><br>
![Alt text](https://github.com/Sabrina-manahil-waseem-006/python-project/blob/main/5.JPG)

---
# 📈 Future expansion: 
Since it was our first project we tried our best but the app will be much better with little improvements 
here and there. Hence, we are planning to make our project even more fun and interesting for kids. We 
plan to add new topics like animals, colors, and shapes to keep things exciting. We're thinking about 
different levels of difficulty, so as kids get better, they can challenge themselves more. We're also 
considering giving out virtual stickers or stars as rewards for correct answers. In the future, we hope to let 
kids play with their friends and family in a multiplayer mode. Parents or teachers might be able to see 
how well kids are doing and help them learn better. We're dreaming up cool ideas like letting kids choose 
backgrounds or themes for the game, and even going on adventures in a story mode
