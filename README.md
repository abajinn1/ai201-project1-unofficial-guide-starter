# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

This project covers unofficial student knowledge about the WGU Bachelor of Science in Cybersecurity and Information Assurance program. The guide focuses on student-shared advice about acceleration, transfer credits, certification preparation, course difficulty, capstone expectations, and common bottlenecks.

This knowledge is valuable because official WGU pages explain the degree structure and requirements, but they do not fully capture what students experience while completing the program. Students often want to know which courses feel hardest, whether one-term completion is realistic, how certifications affect progress, and how to prepare for certification-heavy courses. That information is hard to find through official channels because it is scattered across Reddit threads, student writeups, and informal discussions rather than being organized in one searchable guide.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| #  | Source                                                     | Type                      | URL or file path                                                                                                                                                         |
| -- | ---------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1  | WGU BSCSIA Program Page                                    | Official program page     | `documents/01_wgu_bscsia_program_page.txt` / https://www.wgu.edu/online-it-degrees/cybersecurity-information-assurance-bachelors-program.html                            |
| 2  | WGU BSCSIA Program Guide PDF                               | Official program guide    | `documents/02_wgu_bscsia_program_guide.txt` / https://www.wgu.edu/content/dam/wgu-65-assets/western-governors/documents/program-guides/information-technology/BSCSIA.pdf |
| 3  | Reddit: Completed BSCSIA in 159 Days                       | Student Reddit writeup    | `documents/03_completed_bscsia_159_days.txt` / https://www.reddit.com/r/WGU/comments/11n8862/completed_bscia_in_159_days_14_classes_master/                              |
| 4  | Reddit: How are people finishing in one term?              | Student Reddit discussion | `documents/04_one_term_acceleration_discussion.txt` / https://www.reddit.com/r/WGU/comments/11suupz/how_are_people_finishing_in_one_term/                                |
| 5  | Reddit: Fast-tracking BSCSIA with Certifications           | Student Reddit discussion | `documents/05_fast_tracking_with_certifications.txt` / https://www.reddit.com/r/WGUCyberSecurity/comments/13iq9ny/seeking_advice_fasttracking_bscsia_at_wgu_with/        |
| 6  | Reddit: Review of the Bachelor's in Cybersecurity Program  | Student Reddit review     | `documents/06_bachelors_cybersecurity_review.txt` / https://www.reddit.com/r/WGUCyberSecurity/comments/1fw9i57/my_review_of_the_bachelors_in_cybersecurity/              |
| 7  | Reddit: Hardest Courses in Cybersecurity Program           | Student Reddit discussion | `documents/07_hardest_cybersecurity_courses.txt` / https://www.reddit.com/r/WGUCyberSecurity/comments/1cwrg2l/what_are_the_hardest_courses_in_the_cybersecurity/         |
| 8  | Reddit: BSCSIA Capstone Done                               | Student Reddit writeup    | `documents/08_bscsia_capstone_done.txt` / https://www.reddit.com/r/WGU/comments/o13eym/bscsia_capstone_done/                                                             |
| 9  | Reddit: WGU Cyber Security Course/Certification List       | Student Reddit discussion | `documents/09_course_certification_list.txt` / https://www.reddit.com/r/WGUCyberSecurity/comments/p9m3c1/wgu_cyber_security_course_certification_list/                   |
| 10 | Reddit: What Courses Will My CompTIA Certifications Cover? | Student Reddit discussion | `documents/10_comptia_transfer_credit_discussion.txt` / https://www.reddit.com/r/WGU/comments/1dhp4v7/what_courses_will_my_comptia_certifications_cover/                 |


---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

Chunk size: 800 characters

Overlap: 120 characters

Why these choices fit your documents:

The source documents are a mix of official program summaries, student Reddit discussions, and informal student writeups. The useful information usually appears in short paragraphs or clusters of related advice about one topic, such as course difficulty, certifications, acceleration, transfer credit, or capstone work. An 800-character chunk is large enough to preserve the surrounding context for a student claim, while still being small enough to avoid combining too many unrelated topics into one embedding.

The 120-character overlap helps reduce the chance that an important explanation is split across two adjacent chunks. For example, one sentence might name a certification or course, while the next sentence explains why students found it difficult or useful. Overlap gives the retriever a better chance of returning a self-contained passage.

Preprocessing:

The system loads .txt files from the documents/ folder. It performs basic cleanup by normalizing line endings, collapsing excessive blank lines, and removing extra spaces/tabs. Each file also includes source metadata at the top, including title, source URL, and source type.

Final chunk count: 10 chunks

Because the current document set contains short source summaries rather than full copied pages or full Reddit thread text, the system produced 10 chunks total: one chunk per source document. This is enough to demonstrate the RAG pipeline end-to-end, but it is also a limitation. A stronger production version would collect longer source excerpts or full text from each source, which would produce more chunks and support more detailed answers.

Sample Chunk 1 — Reddit: Completed BSCSIA in 159 Days

Source file: documents/03_completed_bscsia_159_days.txt

This student source is about completing the BSCSIA quickly and is useful for questions about acceleration, pacing, and workload. The main student insight is that fast completion depends heavily on prior experience, transfer credits, available study time, and a disciplined course strategy. It should not be treated as a guarantee that every student can finish quickly. It is a student-experience source, not an official WGU promise.

Sample Chunk 2 — Reddit: Fast-tracking BSCSIA with Certifications

Source file: documents/05_fast_tracking_with_certifications.txt

This source covers student discussion about using previous certifications and transfer credits to reduce the number of WGU courses a student needs to complete. It is useful for questions about acceleration through prior learning. The important student insight is that certifications can help, but the exact course coverage depends on WGU's transfer evaluation and current policies. Students should verify equivalencies rather than assuming every certification will apply.

Sample Chunk 3 — Reddit: Hardest Courses in Cybersecurity Program

Source file: documents/07_hardest_cybersecurity_courses.txt

This student discussion is useful for identifying courses or certifications that students often describe as difficult or time-consuming. Common bottlenecks in cybersecurity degree discussions include certification-heavy courses, security exam preparation, technical courses, database-related requirements, and capstone work. Difficulty varies by background: students with IT or cybersecurity experience may find some courses easier, while students new to the field may need more preparation time.

Sample Chunk 4 — Reddit: How are people finishing in one term?

Source file: documents/04_one_term_acceleration_discussion.txt

This student discussion focuses on whether finishing a WGU degree in one term is realistic. Students commonly point out that one-term completion usually requires a combination of transfer credits, prior knowledge, certification experience, strong time management, and many hours per week. The thread is useful because it captures the difference between possible and typical. It helps the guide answer questions about acceleration without overstating what is realistic for every student.

Sample Chunk 5 — Reddit: BSCSIA Capstone Done

Source file: documents/08_bscsia_capstone_done.txt

This source is useful for questions about later-stage BSCSIA work, especially the capstone. Student capstone posts often describe how students organize the final project, what kind of planning is needed, and how prior coursework connects to the final deliverable. The guide should treat capstone advice as student experience rather than official grading policy, and should encourage users to follow the current WGU rubric and course instructions.

---

## Embedding Model

Model used: sentence-transformers/all-MiniLM-L6-v2

The system uses all-MiniLM-L6-v2 through ChromaDB’s SentenceTransformer embedding function. This model was a practical choice because it runs locally, is fast, does not require an API key, and is appropriate for a small student-knowledge corpus.

Top-k used: 5 retrieved chunks per query

I used top-k 5 because student advice can be spread across multiple sources. A single query about acceleration, certifications, or course difficulty may need context from more than one source. Retrieving too few chunks could miss relevant student experience; retrieving too many could introduce unrelated or conflicting information.

Production tradeoff reflection:

If I were deploying this system for real users and cost were not a constraint, I would test multiple embedding models instead of choosing one based only on convenience. Important tradeoffs would include retrieval accuracy, latency, cost, context length, multilingual support, and performance on informal student language. A stronger API-hosted embedding model might handle acronyms, course codes, certification names, and informal Reddit wording better than a small local model. However, local embeddings are cheaper, private, and easier to run without rate limits. For a production system, I would compare models against a fixed evaluation set and choose based on measured retrieval quality rather than assumptions.

Retrieval Test 1

Query: What do students say are common ways to accelerate the WGU BSCSIA program?

Top returned chunks:

Reddit: Completed BSCSIA in 159 Days — distance 0.262
Reddit: Fast-tracking BSCSIA with Certifications — distance 0.276
WGU BSCSIA Program Guide PDF — distance 0.368
Reddit: BSCSIA Capstone Done — distance 0.393
WGU BSCSIA Program Page — distance 0.470

Why the returned chunks are relevant:

The top two chunks are directly relevant. The first discusses fast completion, pacing, workload, prior experience, transfer credits, available study time, and disciplined course strategy. The second discusses certifications and transfer credits as ways to reduce required coursework. The official WGU sources are less specific to acceleration, but they provide baseline program context.

Retrieval Test 2

Query: What do students say are some of the hardest or most time-consuming parts of the WGU cybersecurity program?

Top returned chunks:

Reddit: Hardest Courses in Cybersecurity Program — distance 0.271
WGU BSCSIA Program Guide PDF — distance 0.352
Reddit: Review of the Bachelor's in Cybersecurity Program — distance 0.416
WGU BSCSIA Program Page — distance 0.450
Reddit: WGU Cyber Security Course/Certification List — distance 0.477

Why the returned chunks are relevant:

The first result is highly relevant because it explicitly discusses difficult and time-consuming parts of the cybersecurity program, including certification-heavy courses, technical courses, database-related requirements, and capstone work. The program review is also relevant because it gives a student-level perspective on which parts of the program may require more time. The official WGU sources are less directly about difficulty but provide degree context.

Retrieval Test 3

Query: What certifications or prior credits can help reduce the number of WGU cybersecurity courses a student needs to complete?

Top returned chunks:

Reddit: WGU Cyber Security Course/Certification List — distance 0.259
Reddit: Hardest Courses in Cybersecurity Program — distance 0.296
WGU BSCSIA Program Guide PDF — distance 0.340
WGU BSCSIA Program Page — distance 0.347
Reddit: Review of the Bachelor's in Cybersecurity Program — distance 0.407

Why the returned chunks are relevant:

The top result is relevant because it discusses how cybersecurity courses relate to industry certifications. The official program sources are also useful because they provide baseline program and certification context. The hardest-courses discussion is partially relevant because certification-heavy courses are often discussed as program milestones, but it is not as directly relevant as the certification list source.

---

## Grounded Generation

System prompt grounding instruction:

The system prompt tells the LLM:

You are The Unofficial Guide, a RAG assistant for student-shared WGU cybersecurity program knowledge. Answer using only the retrieved context provided by the user message. Do not use outside knowledge, assumptions, or general knowledge. If the context does not contain enough information to answer, say that the loaded documents do not provide enough information. Cite the source title or source number for every claim.

This grounding instruction is designed to prevent the model from answering from general knowledge. The retrieved chunks are inserted into the prompt as numbered source blocks, each containing the source title, URL, and chunk text. The model is instructed to cite source titles or source numbers for every claim.

How source attribution is surfaced in the response:

Source attribution is surfaced in two ways. First, the answer text includes source numbers and/or source titles. Second, the interface displays a separate “Retrieved sources” box showing each retrieved source, distance score, URL, and chunk preview. This makes the answer traceable to the retrieved documents.

Out-of-scope behavior:

When the documents do not contain enough information, the system is expected to say so instead of inventing an answer. For example, when asked which WGU instructor is best, the system refused to answer because the loaded documents do not include instructor reviews.

Example Response 1 — Successful grounded answer

Question: What do students say are common ways to accelerate the WGU BSCSIA program?

System response:

According to student insights, common ways to accelerate the WGU BSCSIA program include leveraging prior experience, transfer credits, available study time, and a disciplined course strategy (Source 1: Reddit: Completed BSCSIA in 159 Days). Additionally, students discuss using previous certifications to reduce the number of courses needed, but note that exact course coverage depends on WGU's transfer evaluation and current policies (Source 2: Reddit: Fast-tracking BSCSIA with Certifications).

Example Response 2 — Successful grounded answer

Question: What do students say are some of the hardest or most time-consuming parts of the WGU cybersecurity program?

System response:

According to student discussions, some of the hardest or most time-consuming parts of the WGU cybersecurity program include certification-heavy courses, security exam preparation, technical courses, database-related requirements, and capstone work (Source 1: Reddit: Hardest Courses in Cybersecurity Program). The difficulty of these courses can vary depending on a student's background, with those having IT or cybersecurity experience potentially finding some courses easier (Source 1). Additionally, student reviews provide insight into program-level challenges, highlighting which parts may feel straightforward and which parts may require more time (Source 3: Reddit: Review of the Bachelor's in Cybersecurity Program).

Example Response 3 — Out-of-scope refusal

Question: Can the documents tell me which WGU instructor is best?

System response:

The loaded documents do not provide enough information to answer which WGU instructor is best, as they primarily discuss program structure, course equivalencies, and student experiences with certifications and acceleration (Source 1, Source 2, Source 3, Source 4, Source 5). None of the sources mention specific instructors or their evaluations.

Query Interface

The project uses a Gradio web interface launched by running:

python app.py

The interface runs locally at:

http://127.0.0.1:7860

Input field:

Your question: a text box where the user enters a question about WGU cybersecurity student advice.

Output fields:

Grounded answer: the generated answer from the LLM, grounded in retrieved chunks.
Retrieved sources: the retrieved source chunks, including source title, distance score, URL, and a chunk preview.

Sample interaction transcript:

User question:

What do students say about finishing the BSCSIA in one term?

System answer:

According to [Source 4: Reddit: How are people finishing in one term?], students discuss that finishing a WGU degree in one term is usually possible with a combination of transfer credits, prior knowledge, certification experience, strong time management, and many hours per week. This source highlights the difference between what is possible and what is typical, emphasizing that one-term completion is not realistic for every student. [Source 4] suggests that students should have a combination of these factors to achieve such rapid completion.

Retrieved sources included:

Reddit: Completed BSCSIA in 159 Days — distance 0.339
Reddit: BSCSIA Capstone Done — distance 0.388
Reddit: Fast-tracking BSCSIA with Certifications — distance 0.442
Reddit: How are people finishing in one term? — distance 0.444
WGU BSCSIA Program Guide PDF — distance 0.454

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question                                                                                                                  | Expected answer                                                                                                                                                                                                  | System response (summarized)                                                                                                                                                                                                                                          | Retrieval quality  | Response accuracy  |
| - | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------ |
| 1 | What do students say are common ways to accelerate the WGU BSCSIA program?                                                | Students commonly mention transferring in credits, using existing certifications, studying consistently, choosing an efficient course order, and dedicating significant weekly time to coursework.               | The system said students accelerate by using prior experience, transfer credits, available study time, disciplined course strategy, and previous certifications.                                                                                                      | Relevant           | Accurate           |
| 2 | What do students say are some of the hardest or most time-consuming parts of the WGU cybersecurity program?               | Students often identify certification-heavy courses, difficult technical courses, database-related courses, PenTest+/security courses, and the capstone as potential bottlenecks, depending on prior experience. | The system identified certification-heavy courses, security exam preparation, technical courses, database-related requirements, and capstone work as difficult or time-consuming.                                                                                     | Relevant           | Accurate           |
| 3 | What certifications or prior credits can help reduce the number of WGU cybersecurity courses a student needs to complete? | CompTIA certifications and other transfer credits may satisfy some course requirements, but the exact coverage depends on WGU’s current transfer policy and the student’s transcript evaluation.                 | The system said CompTIA and other certification exams may help reduce course requirements, but students must verify current requirements and WGU transfer evaluation.                                                                                                 | Relevant           | Accurate           |
| 4 | What advice do students give for preparing for cybersecurity certification courses at WGU?                                | Students generally recommend using outside study resources, practice exams, structured study plans, and focusing on certification objectives rather than relying only on course material.                        | The system said the documents discuss certifications as major milestones and mention that prior IT/cybersecurity experience may reduce preparation time, but it also admitted that specific certification preparation advice is not provided in the loaded documents. | Partially relevant | Partially accurate |
| 5 | What do students say about finishing the BSCSIA in one term?                                                              | Some students report finishing quickly or in one term, but it usually requires prior knowledge, transfer credits, strong time commitment, and careful pacing; it is not realistic for every student.             | The system said one-term completion is possible but usually requires transfer credits, prior knowledge, certification experience, strong time management, and many hours per week; it also said one-term completion is not realistic for every student.               | Relevant           | Accurate           |


**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<Question that failed or partially failed:

What advice do students give for preparing for cybersecurity certification courses at WGU?

What the system returned:

The system returned a partially useful answer. It said students discuss CompTIA and other certification exams as major milestones in the program. It also said students with prior IT or cybersecurity experience may find some courses easier, while students new to the field may need more preparation time. However, it also stated that specific advice for preparing for cybersecurity certification courses was not provided in the loaded documents.

Root cause tied to a specific pipeline stage:

The root cause was document coverage, not the LLM generation step. The retriever found certification-related chunks, but the documents only contained high-level summaries about certifications, course mappings, and prior experience. They did not contain detailed preparation advice such as practice exams, outside study resources, structured study plans, or certification objective review strategies. Since the LLM was instructed not to use outside knowledge, it correctly avoided inventing unsupported advice.

What I would change to fix it:

I would add more detailed source documents specifically about certification preparation, such as student writeups about Security+, Network+, CySA+, PenTest+, and other certification-heavy WGU courses. I would also add documents that include concrete preparation strategies, study resources, practice exam recommendations, and timelines. With better document coverage, retrieval would have more relevant chunks and the model could produce a more complete grounded answer.

---

## Spec Reflection

One way the spec helped you during implementation:

The planning.md spec helped guide the implementation by forcing me to define the domain, sources, chunking strategy, retrieval approach, evaluation questions, and AI tool plan before coding. This made the implementation more focused because the app had a clear target: WGU cybersecurity student advice rather than a vague general college guide. The spec also helped me choose concrete settings like 800-character chunks, 120-character overlap, top-k 5 retrieval, ChromaDB, and all-MiniLM-L6-v2.

One way your implementation diverged from the spec, and why:

The implementation diverged from the ideal source plan because the final documents were short source summaries rather than full copied Reddit threads or full extracted webpage text. This happened because the project needed to be completed quickly and reliably without spending too much time on scraping, JavaScript-rendered pages, or blocked requests. As a result, the system produced only 10 chunks total, which is enough to demonstrate the full RAG workflow but limits how detailed the answers can be. In a stronger version, I would collect longer source excerpts and rerun the chunking/evaluation process.

---

## AI Usage

Instance 1

What I gave the AI: I gave ChatGPT the project instructions, grading rubric, planning template, and my chosen domain of WGU cybersecurity student advice. I also provided the required planning.md section headers and asked for help making a complete plan before implementation.
What it produced: ChatGPT helped draft the domain explanation, document source list, chunking strategy, retrieval approach, evaluation questions, anticipated challenges, architecture diagram, and AI tool plan.
What I changed or overrode: I reviewed the plan step by step before moving into implementation. I chose to prioritize a fast local .txt document approach instead of live web scraping because it was more reliable for submission. I also verified that the plan matched the rubric before committing it.

Instance 2

What I gave the AI: I gave ChatGPT my planning.md strategy, the starter repo structure, the installed dependencies, and the requirement to build ingestion, chunking, embedding, retrieval, grounded generation, and a query interface.
What it produced: ChatGPT produced a single app.py implementation using local .txt document loading, basic cleaning, 800-character chunking with 120-character overlap, ChromaDB, all-MiniLM-L6-v2, Groq llama-3.3-70b-versatile, and a Gradio interface.
What I changed or overrode: I tested the code locally, found that app.py was accidentally created inside the documents/ folder, moved it to the project root, and reran the app successfully. I verified the system by running all five evaluation questions plus an out-of-scope query, then documented the partial failure caused by limited source coverage.

Instance 3

What I gave the AI: I gave ChatGPT the system outputs from the Gradio app, including retrieved sources, distance scores, and generated answers for the evaluation questions.
What it produced: ChatGPT helped organize the results into README-ready evaluation notes, including expected answers, actual answers, retrieval quality, response accuracy, and a failure case explanation.
What I changed or overrode: I treated the actual app output as the source of truth. When the certification-preparation question returned only partial information, I documented it as a real limitation instead of rewriting it to look perfect.

How to Run
Clone the repository.
Create and activate a virtual environment:
py -3.12 -m venv .venv
source .venv/Scripts/activate
Install dependencies:
python -m pip install -r requirements.txt
python -m pip install gradio
Copy .env.example to .env and add a Groq API key:
cp .env.example .env

The .env file should contain:

GROQ_API_KEY=your_key_here
Run the app:
python app.py
Open the local Gradio URL:
http://127.0.0.1:7860


