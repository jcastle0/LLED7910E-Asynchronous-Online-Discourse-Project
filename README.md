# The Discourse of Asynchronous Online Discussions

## Introduction

With the continued rise in popularity of online courses, examining the nature of how learners in those courses interact is crucial to understanding the knowledge construction process in those courses. This project will attempt to begin to articulate the big "D" Discourse associated with participation in asynchronous discussions in fully online higher education courses. In this case, Discourses are defined as the "ways of behaving, interacting, valuing, thinking, believing, speaking and, often, reading and writing" (Gee, 2015, p.4). In order to analyze the Discourse of asynchronous discussions, I have analyzed data from the learning management system at a large university in the southeastern United States. The dataset spans eight semesters (Spring 2013 - Summer 2015), and contains 225,691 discussion posts from across 7,581 topics. This research will address the following questions:

1. How are asynchronous discussions used in fully online courses?
2. What are the characteristics of academic asynchronous discussions in fully online courses?
3. Who participates in academic asynchronous discussions in fully online courses?
4. To what extent do people participate in academic asynchronous discussions in fully online courses?
5. What specific behaviors do we see across Discourse in academic asynchronous discussions in fully online courses?

This project is meant to be foundational towards my larger research agenda into learner-to-learner interaction, which will include research on asynchronous discussion board use in fully online courses. I intend for my work on this progress to evolve into a paper to be put forth for publication, but such a paper was too large in scope for my work this semester.

## About the Dataset

### Ethical/Privacy Concerns

The mechanisms I am using to gather the data for this project are somewhat new to higher education and largely unexplored at the university where the research is being conducted. As such, there are not existing protocols for the exact situation of this research within the context of this research. In working with IRB, the following factors were taken into account:

1. The research being done here does not involve an intervention. It is simply the collection of existing data.
2. No additional action is being asked of anyone for the purpose of this research. Therefore, this is considered not human subjects research.
3. It is possible to encrypt the identification information of the individuals whose data is being used for this research. Therefore, it is possible to examine the behavior of individuals within and across courses without knowing who the individual is.

These factors were important for gaining IRB approval to conduct this research. Because the research is considered "Not Human Subjects" research and the identification of the individuals whose data is being used is being obfuscated from the researcher by way of encryption, the research was able to move forward without gaining the explicit consent of every individual whose data was collected. The requirement to gain such consent would have rendered the research effectively impossible, as there are 6,339 unique individuals whose data is represented in this dataset. Being required to collect explicit consent from that many distributed individuals, some of whom are likely no longer active at the institution where the research is being conducted, would have made this research infeasible.

With the level of access to data required to conduct this analysis, the researcher must take the ethics of this research very seriously. First, the discussion posts made in online courses should be considered sacred. That is, those posts are written in a community of learners, and those communities should be seen as safe spaces where students are free to express themselves and collaborate on their learning journies. These are not open communities where anyone can come in and read these conversations as a lurker. As such, this research will not reproduce the exact posts of any individual. I believe there is a time and place for such items to be republished for examination, but within the scope of the research currently undertaken it would be a line too far to replicate content written in a private space verbatim for the purpose of this research. Therefore, this research will examine general behaviors and trends of people who participate in ansynchronous online discussions for the purpose of understanding the Discourse that happens in those spaces, but I will not expose the writing of any of the 6,339 individuals whose data was gathered for this analysis.

### Technologies Used in Working with the Dataset

In order to gather this data, the researcher used the application programming interface (API) for the learning management system (LMS) that is used at the institution where the research was conducted. The data was gathered using the Python programming language, and it was stored in the MongoDB database system. The data analysis for this project was conducted using the Python programming language and Google Sheets. The majority of the Python scripts written in the course of this project [can be viewed here](https://github.com/jcastle0/LLED7910E-Asynchronous-Online-Discourse-Project/tree/master/Data%20Analysis%20Scripts).

## How Asynchronous Discussions are Used

In working with this dataset, I identifies several broad categories for how asynchronous discussions are used in online courses. Those categories are as follows:

- Help
- Introductions
- Academic
- Group Workspaces
- General Discussion

Each of these classifications are breifly described below:  

*Help:* These are discussions designed for students to ask for help with various course elements. Often, these discussions focus on technological help and course logistics help.  

*Introductions:* These discussions are designed as a mechanism for students to get to know one another. They usually occur at the beginning of the course, often as one of the first course activities.  

*Academic:* These discussions usually involve the instructor posting a prompt and the students responding to the prompt. The students are usually then expected to reply to one another's thoughts via threaded discussions where posts and replys are linked together. These are the types of dicussions this project attempts to unpack.  

*Group Workspaces:* These discussions are used by students who are working on group projects or undertaking some other activity as a group. Commonly, these discussions last over longer durations, as students use the asynchronous discussions to coordinate group activities.  

*General Discussions:* These discussions are often academic in nature, however the instructor does not provide a prompt. Rather, the students are given free reign to post about whatever comes to mind in relation to a given unit of instruction.  

### The Process of Identifying Useful Data

With 7,581 discussion topics represented in the dataset, my first task was to identify the discussion topics that are relevant to the research I am conducting (specifically, *academic* topics as described above). In order to do this, I built a spreadsheet with all of the discussion names and prompts listed. Then, reading each of the 7,581 discussion prompts, I made a snap judgement as to which category the discussion likely fell into. Often, this was clear. For example, "Introduction" discussions are commonly titled "Introduce Yourself" or "Introduction." Other times, the intent of the disucssion was not as clear. In those cases, if the discussion could reasonably have been academic in nature, I marked it "Academic".

After the process of tagging all 7,581 discussion topics was complete, I had 6,803 topics tagged as "Academic". I then took a random sampling of 2% of those topics (136) and examined those topics in depth. Upon examining each of the 136 topics, I made a determination as to whether or not the topic was "Academic" in the sense described in the above section. Of the 136 topics, I found 68 of meet the criteria for academic usage. I then calculated a series of descriptive statistics on those 68 topics. Those statistics can be viewed in the table below:

| Statistic     | Mean          | Median    | Standard Deviation |
| ------------- | ------------- | --------- | ------------------ |
| Posts per Instructor  | 2.56 | 0.00 | 5.75 |
| Posts per Student  | 2.81 | 2.45 | 1.24 |
| Number of Instructors | 0.41 | 0.00 | 0.50 |
| Number of Students | 11.68 | 10.50 | 8.02 |
| Number of Threads | 11.22 | 7.50 | 10.23 |
| Number of Original Posts Per Student | 0.93 | 1.00 | 2.67 |
| Topic Duration in Days | 8.38 | 6.00 | 8.47 |

Of these data, I determined that *Posts per Instructor* and *Number of Instructors* were not useful for identifying academic discussions because it is very common practice for instructors to communicate with students outside of the discussion areas. The median posts per instructor and number of instructors at zero was indicative of this practice. Additionally, the standard deviations for number of students and number of threads are both quite high. This is likely because there are wide variations in class size among the sampled discussion topics. Using the data generated from this sample of 68 academic discussions, I applied a set of filters to the 6,803 topics that I had previously labeled as "Academic". The filters used as a result of this analysis are as follows:

| Criteria  | Filter    | Rationale |
| --------- | --------- | --------- |
| Length of Discussion | Less than 15 Days | The sample showed that the mean was just over eight days, and the standard deviation was approximately another eight days. Given this data, setting a parameter of two weeks made sense. |
| Number of Original Posts Per Student | Greater than .65 | The mean value for the sample was .93, with a standard deviation of .34. This indicates that often in academic style discussions, students are expected to make a single original post, but students do not always meet that expectation. Therefore, this filter is meant to reflect any discussion topic where at least 65% of students meet the expectation of making an original post. |
| Number of Students | Greater than 2 | In examining the sample topics, I found that topics with fewer than three students were often group work spaces. |
| Posts Per Student | Between 1.5 and 6.8 | This filter reflects a range from one standard deviation below the sample mean up to the maximum value for this criteria from all the sample topics. |

Upon applying these filters to the 6,803 topics previously marked as academic, I was left with 2,260 topics made up of 82,730 discussion posts. This represents the dataset that is used throughout the project. As this project continues to grow, I plan to have other people undertake a process similar to the one described here to see if they arrive at similar numbers in order to strengthen inter-rater reliability.

## Characteristics of Academic Asynchronous Discussions

Using this filtered, focused dataset, my next goal was to broadly describe the characteristics of asynchronous online discussions. I found this important to building the concecpt of the Discourse of asynchronous online discussions because these discussion areas are unique spaces. I did not want to assume that these spaces mirror classrooms or other learning environments. Conversly, I wanted to begin with no assumptions regarding the makeup of these discussions.

## Who Posts in Asynchronous Online Discussions?

The 2,260 discussion topics I analyzed were dominated by student created content. Of the 82,730 discussion posts in those discussions, 76,351 (93.2%) of them were created by students. Another 5,228 (6.4%) of them were created by instructors, and the remaining posts were made by teaching assistants and people in various support roles. Additionally, I performed a word count on the discussion posts from these topics. The total word count across all 82,730 posts was 13,512,291 words. Students were responsible for the creation of 13,102,165 (97%) of those words. On average, a student's post consisted of 172 words, and an instructor's post consisted of 75 words.

While it is clear that there would be many more student posts than instructor posts (there are many more instructors than students, after all), I also checked to see how many topics had any instructor activity in them at all. Of the 2,260 discussion topics analyzed, 873 (38.9%) of them contained at least one post from someone with the role of instructor, and 1,373 (61.1%) contained no instructor posts at all. The presence of teaching assistants much lower, with only 2.6% of discussion topics having any presence from someone with the role of teaching assistant.

These data make it clear that asynchronous online discussions are the domain of students. What cannot be known from this dataset is the extent to which each instructor took steps to help shape the use of discussions in each course. One of my working hypothoses is that the expectation set by the instructor will have a profound effect on the usage of asynchronous discussions by students in a course. In the following sections, I will examine some specific behaviors uncovered as a result of this analysis and tie those behaviors back into this student-dominated discussion space.

## Specific Behaviors Found in the Discourse of Academic Asynchronous Discussions

### The Phenomena of the Orphan Post

### The Phenomena of Overactive and Underactive Students
