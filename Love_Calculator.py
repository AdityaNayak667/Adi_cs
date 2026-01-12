def love_calculator(name1, name2):
    # Combine both names and convert to lowercase
    combined = (name1 + name2).lower()
    
    # Count famous letters for "TRUE LOVE"
    t = combined.count('t')
    r = combined.count('r')
    u = combined.count('u')
    e = combined.count('e')
    
    l = combined.count('l')
    o = combined.count('o')
    v = combined.count('v')
    e2 = combined.count('e')  # e is counted twice
    
    # Calculate two digits
    true_score = t + r + u + e
    love_score = l + o + v + e2
    
    # Final percentage (most popular way)
    percentage = int(str(true_score) + str(love_score))
    
    # Make it between 0-100 (some versions cap it)
    if percentage > 100:
        percentage = 99  # dramatic effect 😏
        
    return percentage


# Main program
print("♥♥♥ LOVE CALCULATOR ♥♥♥")
name1 = input("Enter first person's name : ").strip()
name2 = input("Enter second person's name : ").strip()

love_score = love_calculator(name1, name2)

print(f"\n{name1} ❤️ {name2}")
print(f"Love Score: {love_score}% 💕")

# Some funny messages
if love_score >= 90:
    print("Wow! Soulmates detected! 💍✨")
elif love_score >= 70:
    print("Very strong connection! Go for it! 🔥❤️")
elif love_score >= 50:
    print("There's definitely something there... 😉")
elif love_score >= 30:
    print("It's complicated... but there's hope! 🥺")
else:
    print("Maybe just good friends? 😅💙")
