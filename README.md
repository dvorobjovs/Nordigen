# Nordigen

Task 1: Fake data

The dates have been randomly generated and sorted to represent the list of consequential dates.

Task 2: Categories

What technologies would you use? Why?

We can try using machine learning algoritghms to cluster the bank transactions. 
They would help us to group the transactions by using the data context patterns.

Is your pipeline real-time, batch processing or lazy-computed? What is the difference between those, and when would you use each?

Considering these are bank transactions, I would use real-time processing. Customes do want to get their transactions processed as soon as possible or in real-time. 
We have seen that banks currently do lose competition in some areas like money transfers to abroad, not only because of the fees. Sometimes you can transfer internationally via bank and it may take few days or an hour or so via money transfer service via 3rd party.

Real-time processing does what is say and processes the data in real-time. If you need data now, this is the way to go.
Batch processing is used when the stakeholder does not require data in real-time, so we can batch it and process in more effiecinet and cost saving manner.
Lazy computation uses only data required and whenever required. Therefore can result in cost/computation savings.

How do you measure performance?

In terms of performance I suppose it depends on what data processing style is being used.
For example, for real time the low event latency would be one of the most important ones along with scalability.
For batch processing that might be I/O metrics, CPU resources used.


Task 3: Versioning

In terms of versioning, there are different platforms which are avaialble for version control/revision. Like Github, Gitlab, Bitbucket, etc.
As a real example, we used free version of Talend orchestration tool that was lacking versioning. Therefore we used Bitbucket for version control.
Whenever changes were made, we used 'git add' for staging the changes, then 'git commit' for commiting them and everntually 'git push' for pushing them to the Bitbucket repositary.
Few times problems arose when the latest changes havent been pulled from the remote repository and someone already made some changes.
So 'git checkout changes' and 'git merge main branch' were used to merge the changes from the branch with the main.
