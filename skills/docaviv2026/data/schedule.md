# Docaviv 2026 — Schedule

כל ההקרנות בפסטיבל, ממוין לפי תאריך ואז שעה. שורה אחת להקרנה. שדות מופרדים ב-`|`.

**עמודות:** date | time | hall_label | venue_he | venue_id | film_slug | title_he | title_en | runtime_min | order_url

**איך משתמשים:**
- `grep '^2026-05-31|' data/schedule.md` — כל ההקרנות בתאריך 31.5.
- `grep 'cinematheque-hall-4' data/schedule.md` — כל ההקרנות באולם 4.
- `grep '|holofiction|' data/schedule.md` — כל ההקרנות של סרט מסוים.

**זמן סיום הקרנה:** `end = time + runtime_min`. אם `runtime_min=0`, הנח 90 דקות וציין שזה מוערך.
**חפיפה:** שתי הקרנות חופפות אם הן באותו תאריך וגם `start_A < end_B` וגם `start_B < end_A`.

---

```
date|time|hall_label|venue_he|venue_id|film_slug|title_he|title_en|runtime_min|order_url
2026-05-28|11:00|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|something-in-tzuriels-gut|תחרות סטודנטים - מקבץ 1|Student Competition — Block 1|84|https://cintlv.presglobal.store/order/127938
2026-05-28|13:30|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|addicts|תחרות סטודנטים - מקבץ 2|Student Competition — Block 2|57|https://cintlv.presglobal.store/order/127747
2026-05-28|16:00|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|shoulder|תחרות סטודנטים - מקבץ 3|Student Competition — Block 3|78|https://cintlv.presglobal.store/order/127939
2026-05-28|18:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|holofiction|הולופיקשן|Holofiction|102|https://cintlv.presglobal.store/order/127729/
2026-05-28|18:30|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|menopause-mystery|תעלומת גיל המעבר|Menopause Mystery|75|https://cintlv.presglobal.store/order/127730/
2026-05-28|18:45|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|shalom|שלום|Shalom|80|https://cintlv.presglobal.store/order/127733/
2026-05-28|19:00|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|%d7%94%d7%90%d7%99%d7%97%d7%95%d7%93|הדרבי האחרון | שעריים x מרמורק|The Last Derby | Sha'arayim x Marmorek|55|https://cintlv.presglobal.store/order/127734/
2026-05-28|20:30|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|a-very-good-boy|ילד טוב מאוד|A Very Good Boy|87|https://cintlv.presglobal.store/order/127735/
2026-05-28|21:00|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|time-and-water|זמן ומים|Time And Water|93|https://cintlv.presglobal.store/order/127740/
2026-05-28|21:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|ritual|פולחן|Ritual|80|https://cintlv.presglobal.store/order/127738/
2026-05-29|10:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|wetland|שלושה צלמים בביצה|Three Photographers in the Wetland|59|https://cintlv.presglobal.store/order/127791
2026-05-29|10:15|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|not-made-for-politics|לא נועדה לפוליטיקה|Not Made For Politics|89|https://cintlv.presglobal.store/order/127741/
2026-05-29|10:30|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|%d7%a1%d7%92%d7%a8|אני רם לוי + סגר|I Am Ram Loevy + Closure|68|https://cintlv.presglobal.store/order/127889
2026-05-29|10:30|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|home-ground|Home Ground|Home Ground|42|https://cintlv.presglobal.store/order/127836
2026-05-29|11:00|5|סינמטק תל אביב - אולם 5|cinematheque-hall-5|the-big-chief|הצ'יף הגדול|The Big Chief|87|https://cintlv.presglobal.store/order/127925
2026-05-29|12:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|the-thing-was-like-that|הדבר היה ככה|The Thing Was Like That|64|https://cintlv.presglobal.store/order/127792
2026-05-29|12:30|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|%d7%90%d7%a0%d7%99-%d7%90%d7%97%d7%9e%d7%93|אני אחמד | הקרנות ושיחה|I Am Ahmad | Screening and Talk|25|https://cintlv.presglobal.store/order/127890
2026-05-29|12:30|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|mailin|מיילין|Mailin|89|https://cintlv.presglobal.store/order/127742/
2026-05-29|12:45|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|one-eye-open|עין אחת פקוחה|One eye open|55|https://cintlv.presglobal.store/order/127837
2026-05-29|14:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|laisha-the-story-of-a-womens-magazine|הסודות של לאשה|The Secrets of LaIsha|56|https://cintlv.presglobal.store/order/127793
2026-05-29|14:30|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|scouting-for-locations-in-palestine|Scouting for Locations in Palestine|Scouting for Locations in Palestine|55|https://cintlv.presglobal.store/order/127892
2026-05-29|14:45|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|hostel-jabotinsky|הוסטל ז׳בוטינסקי|Hostel Jabotinsky|60|https://cintlv.presglobal.store/order/127838
2026-05-29|15:00|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|a-world-gone-mad-the-war-diaries-of-astrid-lindgren|עולם מוטרף - יומניה של אסטריד לינדגרן|A World Gone Mad - The War Diaries Of Astrid Lindgren|95|https://cintlv.presglobal.store/order/127743/
2026-05-29|15:45|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|the-meteorite-gang|The Meteorite Gang|The Meteorite Gang|95|https://cintlv.presglobal.store/order/127794
2026-05-29|16:45|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|the-mystery-package|החבילה המסתורית|The Mystery Package|82|https://cintlv.presglobal.store/order/127839
2026-05-29|18:30|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|bodyguard-of-lies|שומרי השקרים|Bodyguard of Lies|90|https://cintlv.presglobal.store/order/127744/
2026-05-29|19:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|drift|דריפט|Drift|104|https://cintlv.presglobal.store/order/127840
2026-05-29|19:15|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|elon-musk-unveiled-the-tesla-experiment|אילון מאסק - הניסוי של טסלה|Elon Musk Unveiled – The Tesla Experiment|90|https://cintlv.presglobal.store/order/127795
2026-05-29|21:00|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|the-best-summer|הקיץ הטוב בעולם|The Best Summer in the World|84|https://cintlv.presglobal.store/order/127745/
2026-05-29|21:30|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|andre-is-an-idiot|אנדריי הוא אידיוט|Andre is an Idiot|87|https://cintlv.presglobal.store/order/127796
2026-05-29|21:30|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|edge-of-the-night|קצה הלילה|Edge Of The Night|92|https://cintlv.presglobal.store/order/127841
2026-05-30|10:00|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|follow-back|תחרות קצרים - מקבץ 1|Follow Back|63|https://cintlv.presglobal.store/order/127894
2026-05-30|10:00|מוזיאון|מוזיאון תל אביב - אודיטוריום אסיה|tel-aviv-museum-asia|ivry-who|Ivry Who?|Ivry Who?|113|https://cintlv.presglobal.store/order/128242
2026-05-30|10:30|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|divia|דיוויה|Divia|79|https://cintlv.presglobal.store/order/127842
2026-05-30|10:30|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|benita|בניטה|BENITA|82|https://cintlv.presglobal.store/order/127746/
2026-05-30|12:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|esther|Esther|Esther|60|https://cintlv.presglobal.store/order/127797
2026-05-30|12:00|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|champ-de-mars|תחרות קצרים - מקבץ 2|Champ De Mars|58|https://cintlv.presglobal.store/order/127895
2026-05-30|12:30|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|jane-elliott-against-the-world|ג'יין אליוט נגד העולם|Jane Elliott Against the World|90|https://cintlv.presglobal.store/order/127843
2026-05-30|12:30|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|the-broken-r|R שבורה|The Broken R|85|https://cintlv.presglobal.store/order/128186
2026-05-30|12:45|מוזיאון|מוזיאון תל אביב - אודיטוריום אסיה|tel-aviv-museum-asia|farruquito-a-flamenco-dynasty|פארוקיטו, שושלת הפלמנקו|Farruquito, A Flamenco Dynasty|90|https://cintlv.presglobal.store/order/128243
2026-05-30|14:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|the-woman-who-didnt-know-how-to-love|THE WOMAN WHO DIDN'T KNOW HOW TO LOVE|THE WOMAN WHO DIDN'T KNOW HOW TO LOVE|80|https://cintlv.presglobal.store/order/127798
2026-05-30|14:00|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|whispers-in-the-woods|Whispers in the Woods|Whispers in the Woods|94|https://cintlv.presglobal.store/order/127893
2026-05-30|14:45|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|the-gaon-family-show|ההצגה של משפחת גאון|The Gaon Family Show|72|https://cintlv.presglobal.store/order/127844
2026-05-30|14:45|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|not-made-for-politics|לא נועדה לפוליטיקה|Not Made For Politics|89|https://cintlv.presglobal.store/order/127844
2026-05-30|15:00|מוזיאון|מוזיאון תל אביב - אודיטוריום אסיה|tel-aviv-museum-asia|i-follow-rivers|I Follow Rivers|I Follow Rivers|92|https://cintlv.presglobal.store/order/128244
2026-05-30|16:30|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|traces|עקבות|Traces|90|https://cintlv.presglobal.store/order/127896
2026-05-30|17:00|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|donn-the-dancer-of-the-xxth-century|דון, רקדן בלט המאה ה-20|Donn — Dancer of the 20th Century|58|https://cintlv.presglobal.store/order/127750/
2026-05-30|17:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|searching-for-haifa-the-story-of-shimon-holy|מחפש את חיפה - הסיפור של שמעון הולי|Searching for Haifa - The story of Shimon Holly|60|https://cintlv.presglobal.store/order/127845
2026-05-30|17:15|מוזיאון|מוזיאון תל אביב - אודיטוריום אסיה|tel-aviv-museum-asia|time-and-water|זמן ומים|Time And Water|93|https://cintlv.presglobal.store/order/128245
2026-05-30|18:45|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|the-big-chief|הצ'יף הגדול|The Big Chief|87|https://cintlv.presglobal.store/order/127897
2026-05-30|18:45|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|soccer-for-the-soul|Saved by the ball|Saved by the ball|96|https://cintlv.presglobal.store/order/127800
2026-05-30|19:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|moshe-mizrahi-climbing-the-mountain|משה מזרחי - לטפס על ההר|Moshe Mizrahi — Climbing the Mountain|88|https://cintlv.presglobal.store/order/127846
2026-05-30|19:30|מוזיאון|מוזיאון תל אביב - אודיטוריום אסיה|tel-aviv-museum-asia|the-thing-was-like-that|הדבר היה ככה|The Thing Was Like That|64|https://cintlv.presglobal.store/order/128246
2026-05-30|21:00|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|a-scary-movie|על הפחד|A Scary Movie|72|https://cintlv.presglobal.store/order/127751/
2026-05-30|21:00|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|natchez|נאצ'ז|Natchez|87|https://cintlv.presglobal.store/order/127898
2026-05-30|21:15|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|do-not-disturb|Do Not Disturb|Do Not Disturb|62|https://cintlv.presglobal.store/order/127801
2026-05-30|21:30|מוזיאון|מוזיאון תל אביב - אודיטוריום אסיה|tel-aviv-museum-asia|drift|דריפט|Drift|104|https://cintlv.presglobal.store/order/128247
2026-05-31|10:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|a-world-gone-mad-the-war-diaries-of-astrid-lindgren|עולם מוטרף - יומניה של אסטריד לינדגרן|A World Gone Mad - The War Diaries Of Astrid Lindgren|95|https://cintlv.presglobal.store/order/127847
2026-05-31|10:00|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|holofiction|הולופיקשן|Holofiction|102|https://cintlv.presglobal.store/order/127940
2026-05-31|11:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|wetland|שלושה צלמים בביצה|Three Photographers in the Wetland|59|https://cintlv.presglobal.store/order/127802
2026-05-31|12:15|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|politzek-the-voices-that-defy-the-kremlin|Politzek - The Voices That Defy The Kremlin|Politzek - The Voices That Defy The Kremlin|90|https://cintlv.presglobal.store/order/127848
2026-05-31|12:30|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|notes-of-a-true-criminal|מיומנו של פושע אמיתי|Notes of a True Criminal|117|https://cintlv.presglobal.store/order/127899
2026-05-31|14:30|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|shalom|שלום|Shalom|80|https://cintlv.presglobal.store/order/127849
2026-05-31|16:30|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|ritual|פולחן|Ritual|80|https://cintlv.presglobal.store/order/127803
2026-05-31|16:45|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|welded-together|לאחות את השברים|Welded Together|96|https://cintlv.presglobal.store/order/127850
2026-05-31|16:45|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|my-family-and-other-clowns|המשפחה שלי וליצנים אחרים|My Family and Other Clowns|84|https://cintlv.presglobal.store/order/127900
2026-05-31|17:45|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|molly-vs-the-machines|פייק ריפורטר | מולי נגד המכונות|Fake Reporter | Molly vs. The Machines|113|https://cintlv.presglobal.store/order/127941
2026-05-31|18:00|5|סינמטק תל אביב - אולם 5|cinematheque-hall-5|description-of-a-struggle|Description of a Struggle|Description of a Struggle|56|https://cintlv.presglobal.store/order/127927
2026-05-31|18:30|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|the-woman-in-white|האישה בלבן|The Woman in White|90|https://cintlv.presglobal.store/order/127804
2026-05-31|19:00|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|lets-assume-for-a-moment-that-god-exists|Let’s Assume, for a Moment, That God Exists|Let’s Assume, for a Moment, That God Exists|70|https://cintlv.presglobal.store/order/127901
2026-05-31|19:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|mamas-girl|ילדה של אמא|Mama's Girl|75|https://cintlv.presglobal.store/order/127852
2026-05-31|20:30|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|land-of-silence-and-darkness|Land of Silence and Darkness|Land of Silence and Darkness|85|https://cintlv.presglobal.store/order/127753/
2026-05-31|21:00|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|%d7%98%d7%99%d7%99%d7%a7-3|מתרסים + טייק 3|Barricades + Take 3|63|https://cintlv.presglobal.store/order/127902
2026-05-31|21:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|lips|שפתיים|Lips|60|https://cintlv.presglobal.store/order/127805
2026-05-31|21:15|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|do-not-disturb|Do Not Disturb|Do Not Disturb|62|https://cintlv.presglobal.store/order/127956
2026-06-01|09:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|kim-novaks-vertigo|הוורטיגו של קים נובאק|Kim Novak’s Vertigo|76|https://cintlv.presglobal.store/order/127806
2026-06-01|10:30|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|jane-elliott-against-the-world|ג'יין אליוט נגד העולם|Jane Elliott Against the World|90|https://cintlv.presglobal.store/order/127853
2026-06-01|13:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|hostel-jabotinsky|הוסטל ז׳בוטינסקי|Hostel Jabotinsky|60|https://cintlv.presglobal.store/order/127854
2026-06-01|13:00|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|the-broken-r|R שבורה|The Broken R|85|https://cintlv.presglobal.store/order/128189
2026-06-01|15:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|one-eye-open|עין אחת פקוחה|One eye open|55|https://cintlv.presglobal.store/order/127855
2026-06-01|15:00|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|a-scary-movie|על הפחד|A Scary Movie|72|https://cintlv.presglobal.store/order/127904
2026-06-01|16:15|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|change-my-mind|שנו את דעתי|Change My Mind|103|https://cintlv.presglobal.store/order/127755/
2026-06-01|16:30|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|moshe-mizrahi-climbing-the-mountain|משה מזרחי - לטפס על ההר|Moshe Mizrahi — Climbing the Mountain|88|https://cintlv.presglobal.store/order/127807
2026-06-01|16:45|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|souvenirs|סובנירים|Souvenirs|75|https://cintlv.presglobal.store/order/127856
2026-06-01|17:00|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|a-song-without-home|שיר ללא בית|A Song Without Home|75|https://cintlv.presglobal.store/order/127903
2026-06-01|18:30|5|סינמטק תל אביב - אולם 5|cinematheque-hall-5|the-gypsies-of-jaffa-never-think-twice|The Gypsies of Jaffa (Never Think Twice)|The Gypsies of Jaffa (Never Think Twice)|65|https://cintlv.presglobal.store/order/127928
2026-06-01|18:45|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|abu-salie|Abu Salie|Abu Salie|75|https://cintlv.presglobal.store/order/127857
2026-06-01|19:00|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|ghost-elephants|Ghost Elephants|Ghost Elephants|99|https://cintlv.presglobal.store/order/127756/
2026-06-01|19:00|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|notes-of-a-true-criminal|מיומנו של פושע אמיתי|Notes of a True Criminal|117|https://cintlv.presglobal.store/order/127905
2026-06-01|19:15|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|face-value|תווי פנים|Face Value|70|https://cintlv.presglobal.store/order/127808
2026-06-01|20:30|5|סינמטק תל אביב - אולם 5|cinematheque-hall-5|%d7%a1%d7%9b%d7%a0%d7%99%d7%9f-%d7%97%d7%99%d7%99|סכנין, חיי|Sakhnin, My Life|50|https://cintlv.presglobal.store/order/127929
2026-06-01|20:30|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|home-ground|Home Ground|Home Ground|84|https://cintlv.presglobal.store/order/127809
2026-06-01|21:15|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|mariinka|מרינקה|Mariinka|94|https://cintlv.presglobal.store/order/127858
2026-06-01|21:30|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|divia|דיוויה|Divia|79|https://cintlv.presglobal.store/order/127757/
2026-06-02|10:30|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|esther|Esther|Esther|60|https://cintlv.presglobal.store/order/127810
2026-06-02|10:45|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|molly-vs-the-machines|פייק ריפורטר | מולי נגד המכונות|Fake Reporter | Molly vs. The Machines|83|https://cintlv.presglobal.store/order/127758/
2026-06-02|11:00|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|change-my-mind|שנו את דעתי|Change My Mind|120|https://cintlv.presglobal.store/order/127906
2026-06-02|12:30|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|menopause-mystery|תעלומת גיל המעבר|Menopause Mystery|75|https://cintlv.presglobal.store/order/127811
2026-06-02|13:00|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|sapiro-v-ford-the-jew-who-sued-henry-ford|שפירו נגד פורד: היהודי שתבע את הנרי פורד|Sapiro v. Ford: The Jew Who Sued Henry Ford|68|https://cintlv.presglobal.store/order/127759/
2026-06-02|14:45|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|the-meteorite-gang|The Meteorite Gang|The Meteorite Gang|95|https://cintlv.presglobal.store/order/127812
2026-06-02|15:15|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|the-campaign|מלחמת הנרטיבים|The Campaign|137|https://cintlv.presglobal.store/order/127760/
2026-06-02|17:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|the-woman-who-didnt-know-how-to-love|THE WOMAN WHO DIDN'T KNOW HOW TO LOVE|THE WOMAN WHO DIDN'T KNOW HOW TO LOVE|80|https://cintlv.presglobal.store/order/127813
2026-06-02|18:30|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|a-goodnight-kiss|נשיקת לילה טוב|A Goodnight Kiss|97|https://cintlv.presglobal.store/order/127761/
2026-06-02|19:00|5|סינמטק תל אביב - אולם 5|cinematheque-hall-5|face-value|תווי פנים|Face Value|70|https://cintlv.presglobal.store/order/127930
2026-06-02|19:15|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|black-gold-the-story-of-israeli-hip-hop|הקרב על ערוץ 13|Black Gold: The Story Of Israeli Hip Hop|81|https://cintlv.presglobal.store/order/127814
2026-06-02|19:30|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|carlos-outside-the-lines|קרלוס מחוץ לקווים|Carlos Outside the Lines|56|https://cintlv.presglobal.store/order/127862
2026-06-02|20:00|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|wax-gold|Wax & Gold|Wax & Gold|97|https://cintlv.presglobal.store/order/127907
2026-06-02|21:15|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|home-ground|Home Ground|Home Ground|42|https://cintlv.presglobal.store/order/127762/
2026-06-02|21:30|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|threes-a-company|Three’s a Company|Three’s a Company|66|https://cintlv.presglobal.store/order/127864
2026-06-03|10:00|5|סינמטק תל אביב - אולם 5|cinematheque-hall-5|reality-vs-algorithm|Reality vs. Algorithm|Reality vs. Algorithm|240|https://cintlv.presglobal.store/order/128560
2026-06-03|10:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|soccer-for-the-soul|Saved by the ball|Saved by the ball|96|https://cintlv.presglobal.store/order/127866
2026-06-03|10:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|the-woman-in-white|האישה בלבן|The Woman in White|84|https://cintlv.presglobal.store/order/127815
2026-06-03|11:00|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|a-goodnight-kiss|נשיקת לילה טוב|A Goodnight Kiss|97|https://cintlv.presglobal.store/order/127763/
2026-06-03|12:15|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|ivry-who|Ivry Who?|Ivry Who?|113|https://cintlv.presglobal.store/order/127816
2026-06-03|14:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|the-meteorite-gang|The Meteorite Gang|The Meteorite Gang|95|https://cintlv.presglobal.store/order/127868
2026-06-03|15:15|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|abu-salie|Abu Salie|Abu Salie|52|https://cintlv.presglobal.store/order/127817
2026-06-03|15:30|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|the-campaign|מלחמת הנרטיבים|The Campaign|137|https://cintlv.presglobal.store/order/127910
2026-06-03|15:30|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|man-on-wire|איש על חבל|Man on Wire|94|https://cintlv.presglobal.store/order/127765/
2026-06-03|16:30|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|the-gaon-family-show|ההצגה של משפחת גאון|The Gaon Family Show|72|https://cintlv.presglobal.store/order/127869
2026-06-03|17:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|the-five-billion-dollar-scam-temporary-name|אין יותר אופציות - עוקץ המליארדים הישראלי|Out of Options|96|https://cintlv.presglobal.store/order/127818
2026-06-03|18:30|5|סינמטק תל אביב - אולם 5|cinematheque-hall-5|la-soufriere|La Soufriere|La Soufriere|31|https://cintlv.presglobal.store/order/127931
2026-06-03|18:45|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|the-orchestra-nous-lorchestre-de-paris|התזמורת|The Orchestra (L'Orchestre de Paris)|90|https://cintlv.presglobal.store/order/127954
2026-06-03|18:45|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|just-sing|פשוט לשיר|Just Sing|93|https://cintlv.presglobal.store/order/127870
2026-06-03|19:30|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|lips|שפתיים|Lips|60|https://cintlv.presglobal.store/order/127820
2026-06-03|20:00|5|סינמטק תל אביב - אולם 5|cinematheque-hall-5|lessons-of-darkness|Lessons of Darkness|Lessons of Darkness|52|https://cintlv.presglobal.store/order/127932
2026-06-03|21:00|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|welded-together|לאחות את השברים|Welded Together|96|https://cintlv.presglobal.store/order/127911
2026-06-03|21:30|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|farruquito-a-flamenco-dynasty|פארוקיטו, שושלת הפלמנקו|Farruquito, A Flamenco Dynasty|90|https://cintlv.presglobal.store/order/127871
2026-06-03|21:30|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|elon-musk-unveiled-the-tesla-experiment|אילון מאסק - הניסוי של טסלה|Elon Musk Unveiled – The Tesla Experiment|90|https://cintlv.presglobal.store/order/127821
2026-06-04|10:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|farruquito-a-flamenco-dynasty|פארוקיטו, שושלת הפלמנקו|Farruquito, A Flamenco Dynasty|90|https://cintlv.presglobal.store/order/127822
2026-06-04|10:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|face-value|תווי פנים|Face Value|70|https://cintlv.presglobal.store/order/127872
2026-06-04|10:15|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|conversations-with-my-dead-friends|שיחות עם החברים המתים שלי|Conversations with My Dead Friends|92|https://cintlv.presglobal.store/order/127766/
2026-06-04|12:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|esther|Esther|Esther|60|https://cintlv.presglobal.store/order/127955
2026-06-04|12:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|the-mystery-package|החבילה המסתורית|The Mystery Package|82|https://cintlv.presglobal.store/order/127823
2026-06-04|12:45|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|carlos-outside-the-lines|קרלוס מחוץ לקווים|Carlos Outside the Lines|56|https://cintlv.presglobal.store/order/127767/
2026-06-04|14:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|ritual|פולחן|Ritual|80|https://cintlv.presglobal.store/order/127873
2026-06-04|14:45|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|mailin|מיילין|Mailin|89|https://cintlv.presglobal.store/order/127768/
2026-06-04|16:15|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|%d7%94%d7%90%d7%99%d7%97%d7%95%d7%93|הדרבי האחרון | שעריים x מרמורק|The Last Derby | Sha'arayim x Marmorek|55|https://cintlv.presglobal.store/order/127874
2026-06-04|16:30|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|do-not-disturb|Do Not Disturb|Do Not Disturb|62|https://cintlv.presglobal.store/order/127824
2026-06-04|16:30|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|kim-novaks-vertigo|הוורטיגו של קים נובאק|Kim Novak’s Vertigo|76|https://cintlv.presglobal.store/order/127913
2026-06-04|17:00|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|mamas-girl|ילדה של אמא|Mama's Girl|75|https://cintlv.presglobal.store/order/127769/
2026-06-04|17:00|5|סינמטק תל אביב - אולם 5|cinematheque-hall-5|promised-lands|ארצות מובטחות|Promised Lands|86|https://cintlv.presglobal.store/order/127933
2026-06-04|18:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|jane-elliott-against-the-world|ג'יין אליוט נגד העולם|Jane Elliott Against the World|90|https://cintlv.presglobal.store/order/127881
2026-06-04|18:30|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|edge-of-the-night|קצה הלילה|Edge Of The Night|92|https://cintlv.presglobal.store/order/127914
2026-06-04|19:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|laisha-the-story-of-a-womens-magazine|הסודות של לאשה|The Secrets of LaIsha|56|https://cintlv.presglobal.store/order/127825
2026-06-04|19:15|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|searching-for-haifa-the-story-of-shimon-holy|מחפש את חיפה - הסיפור של שמעון הולי|Searching for Haifa - The story of Shimon Holly|60|https://cintlv.presglobal.store/order/127770/
2026-06-04|20:00|5|סינמטק תל אביב - אולם 5|cinematheque-hall-5|my-best-fiend|חברי הטוב ביותר|My Best Fiend|95|https://cintlv.presglobal.store/order/127934
2026-06-04|20:30|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|one-eye-open|עין אחת פקוחה|One eye open|55|https://cintlv.presglobal.store/order/127882
2026-06-04|21:00|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|a-very-good-boy|ילד טוב מאוד|A Very Good Boy|87|https://cintlv.presglobal.store/order/127915
2026-06-04|21:15|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|benita|בניטה|BENITA|82|https://cintlv.presglobal.store/order/127771/
2026-06-05|10:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|threes-a-company|Three’s a Company|Three’s a Company|66|https://cintlv.presglobal.store/order/127827
2026-06-05|11:00|5|סינמטק תל אביב - אולם 5|cinematheque-hall-5|follow-back|תחרות קצרים - מקבץ 1|Follow Back|63|https://cintlv.presglobal.store/order/127935
2026-06-05|11:30|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|the-woman-in-white|האישה בלבן|The Woman in White|84|https://cintlv.presglobal.store/order/127883
2026-06-05|12:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|black-gold-the-story-of-israeli-hip-hop|הקרב על ערוץ 13|Black Gold: The Story Of Israeli Hip Hop|120|https://cintlv.presglobal.store/order/127828
2026-06-05|12:00|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|mariinka|מרינקה|Mariinka|94|https://cintlv.presglobal.store/order/127917
2026-06-05|13:00|5|סינמטק תל אביב - אולם 5|cinematheque-hall-5|champ-de-mars|תחרות קצרים - מקבץ 2|Champ De Mars|58|https://cintlv.presglobal.store/order/127936
2026-06-05|14:15|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|the-musician-and-the-whale|המוזיקאי והליוותן|The Musician and the Whale|83|https://cintlv.presglobal.store/order/127918
2026-06-05|14:15|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|the-thing-was-like-that|הדבר היה ככה|The Thing Was Like That|64|https://cintlv.presglobal.store/order/128194/
2026-06-05|16:00|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|underdogs-a-war-movie|Underdogs: A War Movie|Underdogs: A War Movie|85|https://cintlv.presglobal.store/order/127774/
2026-06-05|16:15|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|sapiro-v-ford-the-jew-who-sued-henry-ford|שפירו נגד פורד: היהודי שתבע את הנרי פורד|Sapiro v. Ford: The Jew Who Sued Henry Ford|68|https://cintlv.presglobal.store/order/127919
2026-06-05|17:00|5|סינמטק תל אביב - אולם 5|cinematheque-hall-5|israel-why|Israel, Why|Israel, Why|207|https://cintlv.presglobal.store/order/127937
2026-06-05|17:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|shalom|שלום|Shalom|80|https://cintlv.presglobal.store/order/127829
2026-06-05|18:15|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|whispers-in-the-woods|Whispers in the Woods|Whispers in the Woods|94|https://cintlv.presglobal.store/order/127772/
2026-06-05|19:30|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|the-woman-who-didnt-know-how-to-love|THE WOMAN WHO DIDN'T KNOW HOW TO LOVE|THE WOMAN WHO DIDN'T KNOW HOW TO LOVE|80|https://cintlv.presglobal.store/order/127830
2026-06-05|21:00|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|the-best-summer|הקיץ הטוב בעולם|The Best Summer in the World|84|https://cintlv.presglobal.store/order/127775/
2026-06-05|21:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|grizzly-man|Grizzly Man|Grizzly Man|103|https://cintlv.presglobal.store/order/127884
2026-06-05|21:30|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|esther|Esther|Esther|60|https://cintlv.presglobal.store/order/127831
2026-06-06|10:00|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|the-orchestra-nous-lorchestre-de-paris|התזמורת|The Orchestra (L'Orchestre de Paris)|90|https://cintlv.presglobal.store/order/127776/
2026-06-06|12:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|face-value|תווי פנים|Face Value|70|https://cintlv.presglobal.store/order/127886
2026-06-06|12:15|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|my-family-and-other-clowns|המשפחה שלי וליצנים אחרים|My Family and Other Clowns|84|https://cintlv.presglobal.store/order/127777/
2026-06-06|12:30|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|the-five-billion-dollar-scam-temporary-name|אין יותר אופציות - עוקץ המליארדים הישראלי|Out of Options|96|https://cintlv.presglobal.store/order/127832
2026-06-06|14:00|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|super-paradise-the-story-of-mykonos|חופי גן עדן: הסיפור של מיקונוס|Paradise Beaches: The Story of Mykonos|88|https://cintlv.presglobal.store/order/127998
2026-06-06|14:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|the-thing-was-like-that|הדבר היה ככה|The Thing Was Like That|64|https://cintlv.presglobal.store/order/127957
2026-06-06|14:30|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|soccer-for-the-soul|Saved by the ball|Saved by the ball|96|https://cintlv.presglobal.store/order/127778/
2026-06-06|15:00|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|do-not-disturb|Do Not Disturb|Do Not Disturb|62|https://cintlv.presglobal.store/order/127833
2026-06-06|16:15|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|the-mystery-package|החבילה המסתורית|The Mystery Package|82|https://cintlv.presglobal.store/order/127999
2026-06-06|17:00|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|hostel-jabotinsky|הוסטל ז׳בוטינסקי|Hostel Jabotinsky|60|https://cintlv.presglobal.store/order/127922
2026-06-06|18:30|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|the-musician-and-the-whale|המוזיקאי והליוותן|The Musician and the Whale|83|https://cintlv.presglobal.store/order/128000
2026-06-06|18:45|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|a-song-without-home|שיר ללא בית|A Song Without Home|75|https://cintlv.presglobal.store/order/127923
2026-06-06|19:15|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|wetland|שלושה צלמים בביצה|Three Photographers in the Wetland|59|https://cintlv.presglobal.store/order/127887
2026-06-06|19:15|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|andre-is-an-idiot|אנדריי הוא אידיוט|Andre is an Idiot|87|https://cintlv.presglobal.store/order/127834
2026-06-06|20:45|2|סינמטק תל אביב - אולם 2|cinematheque-hall-2|threes-a-company|Three’s a Company|Three’s a Company|66|https://cintlv.presglobal.store/order/127924
2026-06-06|20:45|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|natchez|נאצ'ז|Natchez|87|https://cintlv.presglobal.store/order/128001
2026-06-06|21:00|1|סינמטק תל אביב - אולם 1|cinematheque-hall-1|elon-musk-unveiled-the-tesla-experiment|אילון מאסק - הניסוי של טסלה|Elon Musk Unveiled – The Tesla Experiment|90|https://cintlv.presglobal.store/order/127888
2026-06-06|21:15|4|סינמטק תל אביב - אולם 4|cinematheque-hall-4|laisha-the-story-of-a-womens-magazine|הסודות של לאשה|The Secrets of LaIsha|56|https://cintlv.presglobal.store/order/127781/
2026-06-06|21:30|3|סינמטק תל אביב - אולם 3|cinematheque-hall-3|drift|דריפט|Drift|104|https://cintlv.presglobal.store/order/127835
```
