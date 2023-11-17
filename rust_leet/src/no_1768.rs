

struct Ttst {
    word1: String;
    word2: String;
}
impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        // let mut max_word = 0;
        // let mut min_loop = word1.len();
        if word1.len() >= word2.len(){
            let max_word = 1;
            let min_loop = word2.len();
            let s1 = &word1[0..min_loop];
            let s2 = &word2[0..min_loop];
            let s3 = &word2[min_loop..];
        }
        else{
            let max_word = 0;
            let min_loop = word1.len();
            let s1 = &word1[0..min_loop];
            let s2 = &word2[0..min_loop];
            let s3 = &word2[min_loop..];
        }
        // let min_loop: i32 = min(word1.len(), word2);
        let mut ans = String::from("");
        
        for i in (0..min_loop).rev() {
            ans.push_str(word1[i]);
            ans.push_str(word2{i});
        }
        println!("{ans}");
        if max_word == 0 {
            for j in (min_loop-1..word2.len()).rev() {
                ans.push_str(word2[j]);
            }
        }
        if max_word == 1 {
            for j in (min_loop-1..word1.len()).rev() {
                ans.push_str(word1[j]);
            }
        }
        println!("{ans}");
    ans
    }
}
