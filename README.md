Introduction
Artificial Intelligence when used with machines, it shows us the capability ofthinking like humans. In this, a computer system is designed in such a way that typicallyrequires interaction from human. As we know Python is an emerging language so itbecomes easy to write a script for Voice Assistant in Python. The instructions for theassistant can be handled as per the requirement of user. Speech recognition is the Alexa,Siri, etc.InPythonthere isanAPI calledSpeech Recognitionwhichallows us toconvert speech into text. It was an interesting task to make my own assistant. It becameeasiertosendemailswithouttypinganyword,SearchingonGooglewithoutopeningthe browser, and performing many other daily tasks like playing music, opening yourfavoriteIDEwiththehelpofasinglevoicecommand.Inthecurrentscenario,advancementintechnologiesaresuchthattheycanperformanytaskwithsameeffectiveness or can say more effectively than us. By making this project, I realized thattheconcept ofAIin every fieldis decreasing humaneffort and savingtime.
As the voice assistant is using Artificial Intelligence hence the result that it isprovidingare highlyaccurateandefficient.The assistantcanhelptoreduce humaneffortandconsumestimewhileperforminganytask,theyremovedtheconceptoftyping completely and behave as another individual to whom we are talking and askingtoperformtask.Theassistantisnolessthanahumanassistantbutwecansaythatthisis more effective and efficient to perform any task. The libraries and packages used tomakethis assistant focuses onthetime complexities andreduces time.
The functionalities include ,It can send emails,It can read PDF,It can send texton WhatsApp, It can open command prompt, your favorite IDE, notepad etc., It can playmusic,ItcandoWikipediasearchesforyou,ItcanopenwebsiteslikeGoogle,YouTube, etc., in a web browser, It can give weather forecast, It can give desktopremindersofyour choice. Itcan havesome basic conversation.
Tools and technologies used are V S Code IDE for making this project, and Icreated all py files in PyCharm. Along with this I used following modules and librariesin my project. pyttsx3, SpeechRecognition, Datetime, Wikipedia, Smtplib, pywhatkit,pyjokes, pyPDF2,   pyautogui, pyQt etc. I have created a live GUI for interacting withtheJARVISas itgives adesign andinterestinglook whilehaving theconversation.
 
In today’s era almost all tasks are digitalized. We have Smartphone in hands and it isnothing less than having world atyour finger tips. These days we aren’t even using fingers.We just speak of the task and it is done. There exist systems where we can say Text Dad, “I’llbe late today.” And the text is sent. That is the task of a Virtual Assistant. It also supportsspecialized task such as booking a flight, or finding cheapest book online from various e-commerce sites and then providing an interface to book an order are helping automate search,discoveryandonlineorderoperations.
Virtual Assistants are software programs that help you ease your day to day tasks, suchas showing weather report, creating reminders, making shoppinglists etc. They can takecommands via text (online chat bots) or by voice. Voice based intelligent assistants need aninvoking word or wake word toactivate thelistener, followedby the command.For myproject the wake word is Jarvis. We have somany virtual assistants, such as Apple’s Siri,Amazon’sAlexaand Microsoft’sCortana.Forthisproject,wake word waschosenJarvis.
Voice searches have dominated over text search. Web searches conducted via mobiledevices have only just overtaken those carried out using a computer and the analysts arealready predicting that 50% of searches will be via voice by 2020.Virtual assistants are turningout to be smarter than ever. Allow your intelligentassistantto make email work foryou.Detect intent, pick out important information, automate processes, and deliver personalizedresponses.
This projectwasstarted on the premise thatthereissufficientamountof openlyavailable data and information on the web that can be utilized to build a virtual assistant thathasaccesstomakingintelligentdecisionsforroutine useractivities
 
Problem statement
Now the basic question arises in mind that how it is an AI? The virtual assistant that we have created is like if it is not an A.I, but it is the output of a bundle of the statement. But fundamentally, the mail purpose of A.I machines is that it can perform human tasks with the same efficiency or even more efficiently than humans. It is a fact that my virtual assistant is not a very good example of A.I., but it is an A.I.
We are familiar with many existing voice assistants like Alexa, Siri, Google Assistant, Cortana which uses concept of language processing, and voice recognition. They listens the command given by the user as per their requirements and performs that specific function in a very efficient and effective manner. But  they have  major drawbacks. 
For Example :
SIRI from Apple :SIRI does not maintain a knowledge database of its own and its understanding comes from the information captured in domain models and data models.
ReQall :Will take some time to put all of the to-do items in – you could spend more time putting the entries in than actually doing the revision. Etc
But for using These assistants one should have an account (like Google account for Google assistant, Microsoft account for Cortana) and can use it with internet connection only because these assistants are going to work with internet connectivity.They are integrated with many devices like, phones, laptops, and speakers etc
There already exist a number of desktop virtual assistants. A few examples of currentvirtual assistants available in market are discussed in this section along with the tasks they canprovideandtheirdrawbacks.
SIRIfromApple
SIRI is personal assistant software that interfaces with the user thru voice interface,recognizes commands and acts on them. It learns to adapt to user’s speech and thus improvesvoice recognition over time. It also tries to converse with the user when it does not identify theuserrequest.It integrates with calendar, contacts and music library applications on the device andalso integrates with GPS and camera on the device. It uses location, temporal, social and taskbased contexts, to personalize the agent behavior specifically to the user at a given point oftime.
SupportedTasks

•	Callsomeonefrommycontactslist
•	LaunchanapplicationonmyiPhone
•	Sendatextmessagetosomeone
•	Setupameeting onmycalendarfor9amtomorrow
•	Setanalarmfor5amtomorrowmorning
•	PlayaspecificsonginmyiTuneslibrary
•	Enteranewnote

Drawback

SIRI doesnot maintainaknowledgedatabaseofitsownanditsunderstandingcomes from theinformationcapturedindomainmodels anddata models.
ReQall

ReQall is personal assistant software that runs on smartphones running Apple iOS orGoogleAndroid operating system. It helps user to recall notes as well as tasks within alocation and timecontext. Itrecords user inputs and converts them intocommands, andmonitors current stack of user tasks to proactively suggest actions while considering anychanges in the environment. It also presents information based on the context of the user, aswell as filter information to the user based on its learned understanding of the priority of thatinformation.
SupportedTasks

•	Reminders
•	Email
•	Calendar,GoogleCalendar
•	Outlook
•	Evernote
•	Facebook, LinkedIn
•	NewsFeeds

Drawback

Willtakesometimetoputalloftheto-doitemsin–youcouldspendmoretime putting theentriesinthanactuallydoingtherevision.
Objectives
Main objective of building personal assistant software (a virtual assistant) is usingsemantic data sources available on the web, user generated content and providing knowledgefrom knowledge databases. The main purpose of an intelligent virtual assistant is to answerquestions that users may have. This may be done in a business environment, for example, onthe business website, with a chat interface. On the mobile platform, the intelligent virtualassistant is available as a call-button operated service where a voice asks the user “What can Idoforyou?”andthenresponds toverbalinput.
Virtual assistants can tremendously save you time. We spend hours in online researchand then making the report in our terms of understanding. Jarvis can do that for you. Provide atopic for research and continue with your tasks while Jarvis does the research. Another difficulttask is to remember test dates, birthdates or anniversaries. It comes with a surprise when youenter the class and realizeitis class test today. Just tell Jarvis in advance about your tests andsheremindsyouwellinadvancesoyoucanprepare forthe test.
One of the main advantages of voice searches is their rapidity. In fact, voice is reputedto be four times faster than a written search: whereas we can write about 40 words per minute,we are capable of speaking around 150 during the same period of time15. In this respect, theability of personal assistants to accurately recognize spoken words is a prerequisite for them tobe adoptedbyconsumers
PURPOSE,SCOPEANDAPPILCABILITY
Purpose

Purpose of virtual assistant is to being capable of voice interaction, music playback,making to-do lists, setting alarms, streaming podcasts, playing audiobooks, and providingweather,traffic,sports,andotherreal-timeinformation,suchasnews.Virtual assistantsenable users to speak natural language voice commands in order to operate the device and itsapps.
There is an increased overall awareness and a higher level of comfort demonstratedspecificallybymillennialconsumers.Inthisever-evolvingdigitalworldwherespeed,efficiency, and convenience are constantly being optimized, it’s clear that we are movingtowards less screeninteraction.

Scope:

Voiceassistantswillcontinuetooffermore individualizedexperiencesastheygetbetter at differentiating between voices. However, it’s not just developers that need to addressthe complexity of developing for voice as brands also need to understand the capabilities ofeach device and integration and if it makes sense for their specific brand. They will also needtofocuson maintaininga userexperience thatis consistentwithin the comingyears ascomplexitybecomesmoreof aconcern.Thisisbecausethevisualinterfacewithvoiceassistantsismissing.Userssimplycannotsee ortoucha voiceinterface.
Applicability: 

The mass adoption of artificial intelligence in users’ everyday lives is also fueling theshift towards voice. The number of IoT devices such as smart thermostats and speakers aregiving voice assistants more utility in a connected user’s life. Smart speakers are the numberone way we are seeing voice being used. Many industry experts even predict that nearly everyapplicationwillintegrate voicetechnologyinsome wayinthe next5years.
The use of virtual assistants can also enhance the system of IoT (Internet of Things).Twentyyearsfromnow,Microsoftanditscompetitorswillbeofferingpersonaldigitalassistants that will offer the services of a full-time employee usually reserved for the rich andfamous.

 
Dataset Explanation
In the Jarvis project, the specific use of a pre-defined dataset may not be required, as the focus is more on real-time interaction and leveraging online resources. However, there are some underlying data sources and APIs that Jarvis can access to gather information. 
The Jarvis project, as a fictional AI assistant, doesn't have a specific API associated with it. However, to create a similar AI assistant like Jarvis, you can use various APIs to integrate different functionalities into your project. Here are some examples of APIs that you could use to implement features like fetching weather information, accessing trending movies, and generating random jokes:

1. Weather API: You can use weather APIs such as OpenWeatherMap, AccuWeather, or Weatherbit to retrieve weather information based on a location. These APIs allow you to access current weather conditions, forecasts, temperature, humidity, wind speed, and other relevant data.
2. Movie API: Services like The Movie Database (TMDb) or IMDb offer APIs that allow you to fetch information about movies, including details like movie titles, descriptions, ratings, release dates, cast and crew information, trailers, and more. You can use these APIs to retrieve information about trending movies, search for specific movies, or get details about popular films.
3. Joke API: Several APIs, such as JokeAPI, Official Joke API, or ICNDB (Internet Chuck Norris Database), provide random jokes or specific joke categories. These APIs allow you to fetch jokes in various formats, including text, JSON, or even programmatically generate jokes.
4. Wikipedia: Jarvis can utilize the Wikipedia API to retrieve information on various topics. It can query the API based on user requests and fetch summaries or specific details from Wikipedia articles.
To access these APIs, you typically need to register for an API key or authorization token. The API key helps to identify and authenticate your requests to the API service. Each API provider has its own documentation that explains how to make requests, what data you can expect in the responses, and any limitations or restrictions that apply.
