

The LLM super coach allows you to put diary entries into llama and have it act as a coach to analyze you.  

Download any llama.cpp model that is safe or not safe depending on your taste.  

* Learn why you're not a billionaire.  (examples/prompts/billionaire.txt)
* Have the model ask you deep probing questions interactively. (examples/prompts/chat/deep-questions.txt)
* Learn how to improve relationships (examples/prompts/build-relationships.txt)
* Learn how to break bad habits. (examples/prompts/changing-habits.txt)
* Learn uncomfortable truths about yourself. (examples/prompts/uncomfrotable-truths.txt)
* Have a great productive day. (examples/prompts/great-productive-day.txt)
* Get suggestions for developing skills. (examples/prompts/developing-skills.txt)
* Find and fix limiting beliefs (examples/prompts/limiting-beliefs.txt)
  
The program with 4000 context size was run on an M1 macbook with 16gb of ram.  You may have to adjust things up or down
based on your setup.

# Install:

```
git clone https://github.com/ggerganov/llama.cpp

cd llama.cpp

make

cd ..

ln -s ./llama.cpp/main .

```

# Download LLM models. 
```
cd models

wget https://huggingface.co/TheBloke/Utopia-13B-GGUF/resolve/main/utopia-13b.Q4_K_S.gguf

cd ..
```

You might have to use a smaller model than 13b if you are on a machine with less than 16gb.

# Examples 

## As Joe, have the llm ask you deep questions about yourself.

./src/process_summary.py ./examples/joe-example-diary.org ./models/Utopia-13B.q4_k_s.gguf  ./examples/prompts/chat/deep-questions.txt --chat

```
Summary: Morning Routine: The diarist woke up hungover from a night of drinking with co-workers, which may have led to oversharing. They plan to address this issue in the future.

Work: At a meeting, the individual felt frustrated as their ideas were not heard due to an obnoxious co-worker, Bob, who frequently interrupts them.

After Work: The diarist visited the gym and engaged in a rigorous workout, finding it enjoyable. They encountered Ben at the gym and had a conversation about dating and life.

Home: Upon returning home, the diarist browsed Reddit and caught up on AI-related news. They express an interest in starting their own AI business one day.

Analyst Commentary: The diarist appears to be struggling with workplace dynamics, as evidenced by the frustration experienced during the meeting and the challenges posed by co-worker Bob. Their social life, however, seems more enjoyable, as shown by the camaraderie with colleagues during after-hours activities. The individual is also interested in AI and has future entrepreneurial aspirations. To improve their overall satisfaction, they might want to address communication issues at work, find strategies to better assert themselves in meetings, and maintain a balance between personal and professional growth.
LLaMA Output: Insights:

1. The diarist has a tendency to overindulge in alcohol, which can lead to regrettable actions and feelings the next day. This suggests that they might benefit from developing healthier coping mechanisms or setting limits on alcohol consumption.
2. At work, the diarist faces challenges with colleagues not listening to their ideas and feeling frustrated. Improving communication skills and assertiveness could help them better articulate their thoughts and feel more valued in the workplace.
3. The diarist enjoys socializing and engaging in conversations about various topics, as shown by their interactions at the gym with Ben and discussing dating and life. This suggests that they thrive in social environments and could benefit from seeking out more opportunities for meaningful connections.
4. The diarist is interested in AI and has aspirations to start their own business in this field. They should consider focusing on personal development, networking, or attending relevant events to further explore this passion and potentially turn it into a successful career.

Deep Question: What specific steps can the diarist take to balance their social life, professional growth, and personal interests while addressing their struggles with alcohol consumption and improving communication in the workplace?
Your input (leave blank to exit): 

```

## Figure out why joe isn't a billionaire yet

./src/process_summary.py ./examples/joe-example-diary.org ./models/Utopia-13B.q4_k_s.gguf  ./examples/prompts/billionaire.txt

```
Joe's diary entry reveals several reasons why he is not currently on the path to becoming a billionaire. Firstly, his focus is scattered across various interests and projects, which prevents him from dedicating sufficient time and resources to any single venture that could potentially generate substantial wealth. Secondly, Joe tends to prioritize personal satisfaction and learning over monetary gains, as evidenced by his decision to work on a non-profit organization instead of focusing on high-reward, high-income opportunities.

Moreover, Joe's lack of a clear financial goal or plan hinders his progress towards billionaire status. He doesn't have specific targets for income growth or investment returns, which makes it difficult for him to measure his success and adjust his strategies accordingly. Lastly, Joe's reluctance to network with wealthy individuals and learn from their experiences may limit his exposure to valuable insights, opportunities, and potential partnerships that could accelerate his journey to becoming a billionaire.

To change his trajectory and increase the likelihood of becoming a billionaire, Joe should:

1. Identify a primary focus or niche: He needs to choose one area where he can excel and create substantial value, whether it's in entrepreneurship, investing, or another high-income field. This will allow him to concentrate his efforts and resources on achieving success in that domain.
2. Prioritize wealth accumulation: Joe should reevaluate his priorities and focus more on generating substantial income and building wealth, while still maintaining a balance between personal satisfaction and financial goals. This may involve shifting his attention away from non-profit work and towards higher-paying opportunities or ventures with greater potential for growth.
3. Set clear financial targets: He should establish specific, measurable financial goals, such as income milestones, investment returns, and net worth targets. This will enable him to track his progress and adjust his strategies as needed.
4. Network with high-net-worth individuals: Joe should actively seek out networking opportunities with successful entrepreneurs, investors, and other high-achievers who can provide guidance, mentorship, and potentially lucrative partnerships or investment opportunities.
5. Develop a comprehensive financial plan: He needs to create a detailed roadmap that includes short-term and long-term strategies for income growth, investing, risk management, and tax optimization. This will help him stay focused and make informed decisions throughout his journey to becoming a billionaire.
6. Continuously learn and adapt: Joe should remain open to learning from his experiences and the successes of others, while also being willing to adjust his strategies and goals as needed based on new information or opportunities that arise.
7. Focus on scalable business models: When pursuing entrepreneurial ventures, he should prioritize projects with high growth potential and scalable business models, which can generate substantial wealth more efficiently than traditional businesses.
8. Diversify investments: In addition to focusing on his primary area of expertise, Joe should explore various investment opportunities, including real estate, stocks, bonds, and alternative assets, to build a diversified portfolio that can generate consistent income and capital appreciation.
9. Maintain discipline and perseverance: Achieving billionaire status requires unwavering dedication, determination, and resilience in the face of setbacks and challenges. Joe must be prepared to make sacrifices and commit significant time and effort to his pursuit of wealth.
10. Seek mentorship and guidance: Throughout his journey, Joe should actively seek out mentors who have achieved billionaire status or are experienced in the fields he is targeting. Their insights and advice can prove invaluable in helping him avoid common pitfalls and accelerate his progress towards becoming a billionaire.

```
