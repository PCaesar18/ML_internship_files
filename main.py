import guidance

# set the default language model used to execute guidance programs
gpt = guidance.llms.OpenAI("gpt-4", token='OPENAI_API_TOKEN')


interview = guidance('''
{{#system~}}
You are a helpful and terse assistant who works for *****. You are reviewing journalists and would-be journalists for an internship.
{{~/system}}

{{#user~}}

Read the following letter and answer the question below in the query box:


first+last name						JUNE 1, 2023
*****@gmail.com						* ***** AVENUE 
www.*****.com					    GLEBE, NEW SOUTH WALES


Dear Sir/Madam,

Similar to the major of Amsterdam’s struggle with the delicate balance of the liberal policies of decriminalized weed and the ‘window ladies’, see Red Light district. 
Have I too, arguably to a less consequential detriment, wrestled with the freedom bestowed upon the composition of a cover letter. 
Tread too much to the one side and you sound akin to the chatbot that is currently on its warpath to replace you. 
Sway the other way, and suddenly,your writing starts to resemble the inhaling effect of those same liberal policies. 
Yet just like the ladies in the red, sometimes a peek behind the curtains, into the room, is warranted. 

First, the signboard outside would offer you an introduction. 
My described innate wide-ranging curiosity would leap to the forefront. 
So too would my enthusiasm for the rapid pace of change in the field of ****** and my enjoyment of wielding these fascinating new AI tools. 
Quantum Computing, Decentralized Autonomous Organizations (DAO’s), and Generative Adversarial Networks have all captured my attention. 
At ABC University my experience with the extracurricular subject called '****,' delivered by a lawyer and a dance teacher, left me flabbergasted by the power of well-crafted words.

Step inside the room and you might notice the range of projects I enjoy exploring. These span from maintaining my corner of the internet at wwww.***.com, to a deep interest in the global affairs of even the tiniest country—a must if you yourself are from one. 
As well as devising ways to convey and teach this to a new cohort of students at the startups I work for.

Now one may ask, what has [this internship] added to that room of mine? 
I would not hesitate to share my passionate appreciation for their witty, intellectual but concise writings. 
The article '****' is permanently stapled to my wall, not because of the fine-tuned humor, but because it wraps a bland topic in an irresistible work of writing. 
Another favorite is the obituaries, such as the one on **** with the prose about unknown men or women inducing goosebumps.
Moreover, I must credit my current level of English proficiency to reading [newspaper] from cover to cover on more than one occasion.

Exiting this room metaphor, what excites me most about this internship is the opportunity to mingle with a team that produces such high-quality journalism. 
While I admit to not having a journalism background, I do possess a deep curiosity for intellectually stimulating discussions. 
This has made me a good friend of the devil's advocate. 
I believe this internship would provide an unparalleled opportunity to deepen my understanding of technological reporting and gain hands-on experience in a globally renowned publication. 
In addition to aiding in some more concise writing skills.

Please reach out to me with additional questions you may have. I am happy to provide further details on competencies, skills, and experience. I look forward to hearing from you soon.

Kind regards,
first+last name



{{query}}

{{~/user}}

{{#assistant~}}
{{gen 'answer' temperature=0 max_tokens=1000}}
{{~/assistant}}

''', llm=gpt)



while True:


    interaction_Question = input("Ask me any personal question. I'll try to answer to the best of my knowledge! Type 'quit' to exit:..." )

    if interaction_Question == 'quit':
        break

    # execute the program
    output = interview(
        query=interaction_Question
    )
    print(output['answer'])