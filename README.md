# Team-10-10---Job-Postings

Team members (role): Tiye Ngachoko (app development), Laura Perkins (data cleaning and ingestion), Masoma Shoayb (machine learning), Ciera Simon (machine learning)

## Project Overview

This project creates a web application where users can input job postings to determine if it is likely to be fraudulent or not.

To achieve this, a Kaggle dataset of job postings with fraudulent marked, was was used to train a RAG LLM.

**add more stuff here about what we are doing**

## Project Breakdown

### Raw Data

The raw data was obtained from [Kaggle](https://www.kaggle.com/datasets/aiexplorer77/internship-scam-detection-dataset) and then stored on Supabase.

The data was then separated into 4 separate tables (*Company details*, *Recruiter details*, *Posting details*, and *Sentiment scores*)  to promote querying by category.

#### Table 1: Company details

This contains all columns pertaining to company details

- `industry`
- `location`
- `company_name`
- `company_size`
- `company_age`
- `linkedin_presence`
- `website_available`
- `dmoain_age_months`


#### Table 2: Recruiter details

This table contains the company's name and indicators of online presence

- `company_name`
- `recruiter_experience_years`
- `recruiter_email_type`
- `suspicious_email_domain`
- `recruiter_response_time_hours`
- `social_media_presence` (recruiter social media presence)

#### Table 3: Posting details

- `posting_date`
- `internship_title`
- `employment_type`
- `work_mode`
- `industry`
- `company_name`
- `stipend` (I will probably change this name to something more intuitive later)
- `job_description_length`

#### Table 4: Sentiment scores

- `posting_date`
- `internship_title`
- `company_name`
- `verification_status`
- `unrealistic_salary_flag`
- `payment_required`
- `registration_fee`
- `grammatical_errors`
- `vague_description_score`
- `urgency_score`
- `keyword_spam_score`
- `fake_certificate_offer`
- `emotional_manipulation_score`
- `phishing_language_score`
- `trust_signal_score`
- `fraud_score`
- `is_fake_posting`
