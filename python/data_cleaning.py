import pandas as pd


# dataframes to parquet
def save_parquet(df, path, index=False):
    df.to_parquet(path, index=index)


# load raw data
jobs = pd.read_csv("data/raw/Fake_Job_Posting_Detection_Dataset.csv")
internships = pd.read_csv("data/raw/fake_internship_detection_dataset.csv")

# all lowercase
jobs.columns = jobs.columns.str.lower()


# unique column names
print(set(jobs.columns) - set(internships.columns))
print(set(internships.columns) - set(jobs.columns))

# columns unique to `jobs`
## job_title, company_type, label, salary_inr

# columns unique to `internships`
## 'company_name', 'posting_date', 'trust_signal_score', 'job_description_length',
## 'recruiter_email_type', 'recruiter_experience_years', 'fake_certificate_offer',
## 'emotional_manipulation_score', 'is_fake_posting', 'work_mode', 'website_available',
## 'registration_fee', 'grammatical_errors', 'fraud_score', 'location', 'phishing_language_score',
## 'urgency_score', 'keyword_spam_score', 'payment_required', 'suspicious_email_domain',
## 'internship_title', 'unrealistic_salary_flag', 'company_age', 'domain_age_months',
## 'recruiter_response_time_hours', 'linkedin_presence', 'industry', 'company_size',
## 'social_media_presence', 'verification_status', 'vague_description_score', 'stipend'

# special note: `job_title` from `jobs` and `internship_title` from `internships` are probably the same

# rename `internship_title` to `job_title`
internships.rename(columns={"internship_title": "job_title"}, inplace=True)

internships.to_parquet("data/clean/internships.parquet")
jobs.to_parquet("data/clean/jobs.parquet")
