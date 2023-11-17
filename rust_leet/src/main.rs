pub struct Solution{}

impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let mut min_loop = 0;
        let s1: &str;
        let s2: &str;
        let s3: &str;
        if word1.len() >= word2.len(){
            min_loop = word2.len();
            s1 = &word1[0..min_loop];
            s2 = &word2[0..min_loop];
            s3 = &word1[min_loop..];
        }
        else{
            min_loop = word1.len();
            s1 = &word1[0..min_loop];
            s2 = &word2[0..min_loop];
            s3 = &word2[min_loop..];
        }
        // println!("{min_loop}");
        let mut ans = String::from("");
        
        for i in 0..min_loop {
            ans.push(s1[i..].chars().next().unwrap());
            ans.push(s2[i..].chars().next().unwrap());
        }
        // println!("{ans}");
        ans.push_str(&s3);
        println!("{ans}");
    ans
    }
}


fn main() {
    // println!("Hello, world!");
    // let sol = Solution {};
    let w1 = String::from("abc");
    let w2 = String::from("1234");
    println!("{}", Solution::merge_alternately(w1,w2))
}