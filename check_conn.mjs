// This MUST be the first thing you import
import 'dotenv/config'; 
import { createClient } from '@supabase/supabase-js';

const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_KEY = process.env.SUPABASE_KEY;

// 1. Individual Validation
let isValid = true;

if (!SUPABASE_URL) {
  console.error("❌ ERROR: SUPABASE_URL is missing or empty.");
  isValid = false;
}

if (!SUPABASE_KEY) {
  console.error("❌ ERROR: SUPABASE_KEY is missing or empty.");
  isValid = false;
}

if (!isValid) {
  process.exit(1); // Exit early if variables are missing
}

// 2. Connection Attempt
const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);

async function testConnection() {
  console.log("Variables loaded. Testing connection...");
  
  try {
    const { data, error } = await supabase.from('notes').select('count', { count: 'exact', head: true });

    if (error) {
      // var error.message = 'no reason given'
      console.error("❌ Connection failed.");
      if (!error.message) {
        console.log("there is no error message");
      } else {
        console.error("Reason:", error.message); // This will show if the Key is invalid
      }
    } else {
      console.log("✅ Successfully connected to Supabase!");
    }
  } catch (err) {
    console.error("❌ An unexpected error occurred:", err.message);
  }
}

testConnection();