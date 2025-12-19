# Deploying to Vercel

This document provides instructions for deploying the DocuMind application to Vercel.

## Prerequisites

- A Vercel account.
- [Vercel CLI](https://vercel.com/docs/cli) installed.

## Deployment Steps

1. **Login to Vercel:**
   ```bash
   vercel login
   ```

2. **Deploy the application:**
   Navigate to the project's root directory and run the following command:
   ```bash
   vercel
   ```

   Vercel will automatically detect the `vercel.json` configuration and deploy the application.

## Important Notes

- **Model Loading:** The application uses a lazy loading mechanism for the language model. The model will be downloaded and loaded on the first request to the `/chat` endpoint. This may cause a delay on the first request.
- **Vector Store:** The current implementation uses ChromaDB as a local vector store. This will not work on Vercel's ephemeral filesystem. For a production deployment, you should switch to a cloud-based vector store like Chroma Cloud, Pinecone, or others. The `chroma_db` directory is ignored in the `.vercelignore` file.
- **Dependencies:** The required Python packages are listed in `requirements.txt`. The `build.sh` script will automatically install these dependencies during the Vercel build process.
- **Environment Variables:** You can manage environment variables in the Vercel project settings.