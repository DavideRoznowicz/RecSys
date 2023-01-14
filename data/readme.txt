-----------
Description
-----------

    This dataset contains social networking and music artist listening information
    from a set of 2K users from Last.fm online music system.
    http://www.last.fm

    The dataset is released in the framework of the 2nd International Workshop on
    Information Heterogeneity and Fusion in Recommender Systems (HetRec 2011)
    http://ir.ii.uam.es/hetrec2011
    at the 5th ACM Conference on Recommender Systems (RecSys 2011)
    http://recsys.acm.org/2011


---------------
Data statistics
---------------

    1892 users
   17632 artists
   92834 user-listened artist relations, i.e. tuples [user, artist, listeningCount]
         avg. 49.067 artists most listened by each user
         avg. 5.265 users who listened each artist


-----
Files
-----

   * artists.dat

        This file contains information about music artists listened by the users.


   * user_artists.dat

        This file contains the artists listened by each user.
        It also provides a listening count for each [user, artist] pair.
